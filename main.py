import time
from utils import createMarkedHTML
from algorithms import brute_force

# it is our template for print all conclusion for all algorithm
def test_algorithm (algo_name,algo_func,text,pattern,output_filename):
    
    print(f"---> {algo_name} <---")

    
    start_time = time.perf_counter()

    matches,comparisons =algo_func(text,pattern)

    
    end_time = time.perf_counter()

    # convert ms
    run_time_ms = (end_time - start_time) *1000

    createMarkedHTML(text,matches,len(pattern),output_filename)

    print(f"pattern : '{pattern}'")
    print(f"Matches that found : {len(matches)}")
    print(f"Comparison times : {comparisons}")
    print(f"Run time : {run_time_ms:.4f}ms")
    print(f"Saved output file : {output_filename}\n")



if __name__ == "__main__":
        test_text = "<HTML> <BODY> WHICH FINALLY HALTS. AT THAT POINT</BODY> </HTML>"
        pattern = "AT THAT"

        test_algorithm("Brute-Force",brute_force,test_text,pattern,"test1_output.html")