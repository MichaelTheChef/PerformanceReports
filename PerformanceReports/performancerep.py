import psutil; import time

def check_memory_usage():
    threshold = 500; processes = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        processes.append(proc)

    processes.sort(key=lambda x: x.info['memory_info'].rss, reverse=True)

    for proc in processes:
        process_name = proc.info['name']
        memory_usage = proc.info['memory_info'].rss / (1024 * 1024)
        
        if memory_usage > threshold:
            print(f"Process '{process_name}' is using too much memory: {memory_usage:.2f} MB")

def check_cpu_usage():
    threshold = 80
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        process_name = proc.info['name']
        cpu_usage = proc.info['cpu_percent']
        
        if cpu_usage > threshold: print(f"Process '{process_name}' is using too much CPU: {cpu_usage}%")

while True: if __name__ == "__main__": check_memory_usage(); check_cpu_usage(); time.sleep(3)
