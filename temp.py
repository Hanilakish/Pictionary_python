import concurrent.futures
import time

def task(n):
    print(f"Task {n} is starting.")
    time.sleep(n)
    print(f"Task {n} is complete.")
    return n*n

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, range(1,6))
    
    print("Rsults:",list(results))
    print("main thread finished.")

if __name__ == "__main__":
    main()