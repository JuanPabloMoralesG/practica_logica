def count_substring(string, sub_string): 
    conut =0
    start = 0
    while True:
        start = string.find(sub_string,start)
        if start == -1:
            break
        conut+=1
        start+=1

    return conut

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)