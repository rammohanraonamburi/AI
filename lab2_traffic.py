import random

class TrafficSignalController:
    def __init__(self, num_lanes):
        self.lanes = []
        for _ in range(num_lanes):
            lane = {
                'vehicles': random.randint(1, 20),        
                'waiting_time': random.randint(1, 15),    
                'priority': random.randint(1, 3)          
            }
            self.lanes.append(lane)

    def calculate_utility(self, lane):
        vehicle_score = lane['vehicles'] * 2  
        waiting_time_score = lane['waiting_time'] * 1  
        priority_score = lane['priority'] * 5  
        
        return vehicle_score + waiting_time_score + priority_score
    
    def evaluate_signal_configurations(self):
        best_utility = -float('inf')
        best_configuration = None
                
        for i in range(16):  
            configuration = [((i >> j) & 1) for j in range(4)]  
            current_utility = 0
            for idx, signal in enumerate(configuration):
                if signal == 1:  
                    current_utility += self.calculate_utility(self.lanes[idx])
            
            if current_utility > best_utility:
                best_utility = current_utility
                best_configuration = configuration
                
        return best_configuration, best_utility
    
num_lanes = 4  
controller = TrafficSignalController(num_lanes)
best_config, best_utility = controller.evaluate_signal_configurations()

print("Lane Details:")
for idx, lane in enumerate(controller.lanes):
    print(f"Lane {chr(65+idx)} - Vehicles: {lane['vehicles']}, Waiting Time: {lane['waiting_time']} minutes, Priority: {lane['priority']}")

print("\nBest Signal Configuration:", best_config)
print("Best Utility Score:", best_utility)
