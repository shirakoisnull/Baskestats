import multiprocessing
import subprocess

def run_file(file_name):
    subprocess.run(['python', file_name])

if __name__ == '__main__':
    file_names = ['login.py', 'player.py', 'team.py', 'championship.py', 'match.py']

    processes = []
    for file_name in file_names:
        process = multiprocessing.Process(target=run_file, args=(file_name,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
