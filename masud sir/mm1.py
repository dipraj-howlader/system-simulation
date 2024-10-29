import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MM1Queue:
    def __init__(self, env, mean_interarrival, mean_service):
        self.env = env
        self.server = simpy.Resource(env, capacity=1)  # Single-server queue
        self.mean_interarrival = mean_interarrival
        self.mean_service = mean_service
        
        # Tracking metrics for animation
        self.queue_lengths = []
        self.utilization_times = []
        self.current_queue_length = 0

    def customer(self):
        """Process for each customer arriving at the queue."""
        arrival_time = self.env.now
        self.current_queue_length += 1  # Customer joins the queue
        with self.server.request() as request:
            yield request  # Wait for the server if it's busy
            
            # Customer is now being served; update queue length
            self.current_queue_length -= 1
            wait_time = self.env.now - arrival_time

            # Service time
            service_time = random.expovariate(1.0 / self.mean_service)
            self.utilization_times.append(service_time)
            yield self.env.timeout(service_time)

    def arrival_process(self, max_customers):
        """Process handling the arrival of customers."""
        for _ in range(max_customers):
            interarrival_time = random.expovariate(1.0 / self.mean_interarrival)
            yield self.env.timeout(interarrival_time)
            self.env.process(self.customer())
            
            # Record current queue length for animation
            self.queue_lengths.append(self.current_queue_length)

def run_simulation(env, queue, max_customers):
    """Run the arrival process."""
    env.process(queue.arrival_process(max_customers))
    env.run()

def animate_queue(queue_lengths, utilization_times, interval=100):
    """Create an animated plot for queue length and server utilization."""
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Set up Queue Length plot
    ax[0].set_title('Queue Length Over Time')
    ax[0].set_xlim(0, len(queue_lengths))
    ax[0].set_ylim(0, max(queue_lengths) + 1)
    line_queue, = ax[0].plot([], [], lw=2, color="skyblue")
    ax[0].set_ylabel('Queue Length')
    
    # Set up Server Utilization plot
    ax[1].set_title('Server Utilization Over Time')
    ax[1].set_xlim(0, len(utilization_times))
    ax[1].set_ylim(0, 1)
    line_util, = ax[1].plot([], [], lw=2, color="salmon")
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Server Utilization')

    def init():
        line_queue.set_data([], [])
        line_util.set_data([], [])
        return line_queue, line_util

    def update(frame):
        # Update Queue Length plot
        xdata = range(frame)
        ydata_queue = queue_lengths[:frame]
        line_queue.set_data(xdata, ydata_queue)

        # Calculate and update Server Utilization plot
        if frame > 0:
            total_utilization_time = sum(utilization_times[:frame])
            utilization = total_utilization_time / (frame if frame > 0 else 1)
            ydata_util = [utilization] * frame
            line_util.set_data(xdata, ydata_util)
        
        return line_queue, line_util

    ani = FuncAnimation(fig, update, frames=len(queue_lengths), init_func=init, blit=True, interval=interval)
    plt.tight_layout()
    plt.show()

# Parameters
mean_interarrival = 2.0  # Mean time between arrivals
mean_service = 1.5       # Mean service time
max_customers = 100      # Total number of customers

# Set up environment and queue
env = simpy.Environment()
queue = MM1Queue(env, mean_interarrival, mean_service)

# Run the simulation
run_simulation(env, queue, max_customers)

# Run animation
animate_queue(queue.queue_lengths, queue.utilization_times)
