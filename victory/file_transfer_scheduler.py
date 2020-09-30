import sched, time
import os, shutil

s = sched.scheduler(time.time, time.sleep)

def check_file():
    print("Ready to check hls-chunks ..." + str(time.time()))
    
    files = [file for file in os.listdir(".") if (file.lower().endswith(".txt"))]
    files.sort(key=os.path.getmtime) 
    
    for file in sorted(files, key=os.path.getmtime):
        print("File is ..." + file + ' , ' + str(os.path.getmtime(file)))
    
def check_some_times():
    s.enter(10, 1, check_file)
    s.enter(20, 1, check_file)
    
    s.run()
    print("Current Time is ..." + str(time.time()))

# ################################################################
# Schedule frequent file checks ... are there any NEW hls-segments
# ################################################################
def schedule_new_chunks_for_transfer():
    check_some_times()
    
    return True