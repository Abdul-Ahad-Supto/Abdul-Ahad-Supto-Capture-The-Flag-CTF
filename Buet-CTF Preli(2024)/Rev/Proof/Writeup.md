# Proof 
## Points - 350
The **server.go** file contains

```go
package main

import (
	"bufio"
	"crypto/md5"
	"fmt"
	"os"
	"strings"
)

func validateHash(hash string) bool {
	shouldstartwith := "3b4913a4"
	return strings.HasPrefix(hash, shouldstartwith)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)
	key, _ := reader.ReadString('\n')
	key = strings.TrimSpace(key)

	license := fmt.Sprintf("name$%s$key$%s", name, key)
	hash := md5.Sum([]byte(license))
	hashString := fmt.Sprintf("%x", hash)

	if validateHash(hashString) {
		flag := os.Getenv("FLAG")
		if flag != "" {
			fmt.Println("Validation successful!")
			fmt.Printf("Flag: %s\n", flag)
		} else {
			fmt.Println("If you are testing in local environment, set the FLAG environment variable")
			fmt.Println("If you are running it against remote environment, contact admin asap")
		}
	} else {
		fmt.Println("The license is not registered or invalid.")
	}
}
```
In the **server.go** file we can see that the server is taking a name and a key from the client and hashing it to md5 hashing algorithm. Now to validate the client the server is checks if the hash starts with "**3b4913a4**". If it does match. the server validates the client and give the flag. So to trigger that problem we need to do hash collition attack. So in terms of hash related problem there is nothing much we can do. So we have to brute force the md5 until it matches with the desired prefix. So to solve the problem we need to be as efficient as possible to use out Pc's best possible computational power. As my pc has i7 11th gen with 16gb ram, I can process 16 worker at a time so here was my code to brute force it



```python
import hashlib
import random
import string
from multiprocessing import Pool

desired_prefix = "3b4913a4"


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def find_matching_hash(start_index, end_index, desired_prefix):
    counter = start_index
    while counter < end_index:

        random.seed(counter)  
        name = generate_random_string(8)
        key = generate_random_string(8)

        input_string = f"name${name}$key${key}"
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()

        if md5_hash.startswith(desired_prefix):
            print(f"Match found! Loop Count: {counter} Name: {name}, Key: {key}, Hash: {md5_hash}")
            return name, key, md5_hash
        counter += 1

def parallel_search(desired_prefix, processes=16): # Change processes according to your pc power
    ranges = [(i * 1000000000, (i + 1) * 1000000000, desired_prefix) for i in range(processes)]
    with Pool(processes=processes) as pool:
        pool.starmap(find_matching_hash, ranges)

if __name__ == "__main__":
    print("Starting the search for a valid name and key...")
    parallel_search(desired_prefix)

```

 After running the code for around 1h we get the answer :-   
#### Match found! seed: 6206003229 Name: Od1uiWsQ, Key: 1VxbH2o9, Hash: 3b4913a44b95085f8c097074ee62ff91

After putting it to the server if gives the flag!

#### Flag - BUETCTF{G6VjZel2DYbziar516JWgWT}