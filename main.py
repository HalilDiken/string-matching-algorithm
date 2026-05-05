import time
import os
import urllib.request
from utils import createMarkedHTML
from algorithms import brute_force,horspool,boyer_moore

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
    
    # ---------------------------------------------------------
    # PART 1 : 4 Small Test Case for All algorithms
    # ---------------------------------------------------------
    test_cases = [
        ("TC1", "<HTML><BODY>WHICH_FINALLY_HALTS. _ _ AT_THAT POINT </BODY></HTML>", "  "),
        ("TC2", "<HTML><BODY>ABC_AT_THAT_XYZ_AT_THAT_END</BODY></HTML>", "AT_THAT"),
        ("TC3", "<HTML><BODY>AAAAAA</BODY></HTML>", "AAA"),
        ("TC4", "<HTML><BODY>THIS_IS_A_TEST</BODY></HTML>", "XYZ")
    ]

    algorithms = [
        ("Brute-Force", brute_force, "BF"),
        ("Horspool", horspool, "HP"),
        ("Boyer-Moore", boyer_moore, "BM")
    ]

    print("="*50 + "\n Small test case begin\n" + "="*50)

    for tc_name, text, pattern in test_cases:
        print(f"\n[{tc_name}] Test is running - Text: {text}")
        for algo_name, algo_func, short_name in algorithms:
            output_name = f"{tc_name}_{short_name}.html"
            test_algorithm(algo_name, algo_func, text, pattern, output_name)

    # ---------------------------------------------------------
    # PART 2: HTML -> Type 1&2 -> 1) Karamazov Brothers 
    #                             2) Crime and Punishment
    #                             3) Bleak House
    #                             4) Bit String 1
    #                             5) Bit String 2
    #                             6) Bit String 3
    # ---------------------------------------------------------
    print("\n" + "="*50 + "\n TYPE 1: Meaningful HTML \n" + "="*50)
    
    
    html_sources = [
        {
            "id": "CrimeAndPunishment",
            "file_name": "Crime and Punishment.html",
            "patterns": ["Raskolnikov", "all", "murder"]
        },
        {
            "id": "TheBrothersKaramazov",
            "file_name": "The Brothers Karamazov.html", 
            "patterns": ["Karamazov", "the", "characteristics"]
        },
        {
            "id": "BleakHouse",
            "file_name": "Bleak House.html",
            "patterns": ["she", "Chancery", "Jarndyce and Jarndyce"]
        },
        {
            "id": "BitString1",
            "file_name": "bit_string1.html",
            "patterns": ["10101", "00000", "1111111111111111"] 
        },
        {
            "id": "BitString2",
            "file_name": "bit_string2.html",
            "patterns": ["11111", "10001", "0000000000000000"] 
        },
        {
            "id": "BitString3",
            "file_name": "bit_string3.html",
            "patterns": ["01010", "11011", "001001001"]
        }
    ]

    for item in html_sources:
        print(f"\n" + "-"*40)
        print(f" PROCESSING: {item['id']} ")
        print("-" * 40)
        
 
        # Read file and send to algorithms
        with open(item["file_name"], "r", encoding="utf-8") as file:
            html_text = file.read()

        # Look all algorithms for each pattern
        for pattern in item["patterns"]:
            print(f"\n>>> '{pattern}' SEARCHING IN {item['id']} <<<")
            for algo_name, algo_func, short_name in algorithms:
                output_name = f"{item['id']}_{pattern}_{short_name}.html"
                test_algorithm(algo_name, algo_func, html_text, pattern, output_name)