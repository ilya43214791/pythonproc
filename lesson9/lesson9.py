import time
import requests
import threading
import multiprocessing


# CPU-bound task (simulated heavy computation)
def encrypt_file(path: str):
    print(f"Processing file from {path} in process {os.getpid()}")
    start_time = time.perf_counter()
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    end_time = time.perf_counter()
    print(f"Encryption task took {end_time - start_time:.2f} seconds")


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    start_time = time.perf_counter()
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    end_time = time.perf_counter()
    print(f"Download task took {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    try:
        image_url = "https://picsum.photos/1000/1000"

        # Start the CPU-bound task in a separate process
        cpu_process = multiprocessing.Process(target=encrypt_file, args=("rockyou.txt",))
        cpu_process.start()

        # Start the I/O-bound task in a separate thread
        io_thread = threading.Thread(target=download_image, args=(image_url,))
        io_thread.start()

        # Wait for both the process and thread to complete
        cpu_process.join()
        io_thread.join()

        print("Both tasks completed.")

    except Exception as e:
        print(f"Error occurred: {e}")
