
**Q1. Create a Bash script**

```bash
#!/bin/bash
touch student.sh
```

**Q2. Run the script and give executable permission**

```bash
bash student.sh
chmod +x student.sh
```

**Q3. Take user input**

```bash
read -p "Enter your name: " name
echo "Hello $name"
```

**Q4. Check age using if/else**

```bash
age=20

if [ $age -gt 18 ]
then
    echo "You are an adult"
else
    echo "You are a minor"
fi
```

**Q5. Take age from the user and check it**

```bash
read -p "Enter your age: " age

if [ $age -gt 18 ]
then
    echo "You are an adult"
else
    echo "You are a minor"
fi
```

**Q6. Check whether a file exists**

```bash
read -p "Enter filename: " filename

if [ -f "$filename" ]
then
    echo "File exists"
else
    echo "File does not exist"
fi
```

**Q7. Print numbers using a for loop**

```bash
for i in 1 2 3 4 5
do
    echo "Number is: $i"
done
```

**Q8. Add two numbers**

```bash
read -p "Enter your first number: " num1
read -p "Enter your second number: " num2

sum=$((num1 + num2))
echo "Sum is $sum"
```

**Q9. Redirect output to a file**

```bash
echo "Sum is $sum" > result.txt
```

**Q10. Append output to a file**

```bash
echo "Sum is $sum" >> result.txt
```

**Q11. Redirect errors**

```bash
ls abc 2> error.txt
```

**Q12. Use stdin redirection**

```bash
cat < names.txt
```

**Q13. Search a keyword in a log file**

```bash
read -p "Enter your search word: " word
grep -i "$word" system.log >> results.txt
```

**Q14. Check a file and save its details**

```bash
read -p "Enter your filename: " file

if [ -f "$file" ]
then
    echo "File exists"
    ls -l "$file" >> fileinfo.txt
else
    echo "File does not exist"
fi
```

**Q15. Check a directory**

```bash
read -p "Enter your directory name: " dir

if [ -d "$dir" ]
then
    echo "Directory exists"
    ls -l "$dir" > files.txt
else
    echo "Directory does not exist"
fi
```

**Q16. Print numbers using a while loop**

```bash
i=1

while [ $i -le 5 ]
do
    echo "Number: $i"
    ((i++))
done
```

**Q17. Use a case statement**

```bash
read -p "Enter your choice: " choice

case $choice in
    1) echo "Monday" ;;
    2) echo "Tuesday" ;;
    3) echo "Wednesday" ;;
    *) echo "Invalid choice" ;;
esac
```

**Q18. Check whether a path is a file or directory**

```bash
read -p "Enter filename or directory: " filename

if [ -f "$filename" ]
then
    echo "File exists"
elif [ -d "$filename" ]
then
    echo "It is a directory"
else
    echo "File does not exist"
fi
```

**Q19. Create and call a function**

```bash
greet() {
    echo "Hello, welcome to Bash!"
}

greet
```

**Q20. Function with an argument**

```bash
greet() {
    echo "Hello $1!"
}

greet "Hamida"
```

**Q21. Function with two arguments**

```bash
add() {
    sum=$(( $1 + $2 ))
    echo "Sum = $sum"
}

add 10 20
```

**Q22. Count lines in a file**

```bash
read filename

if [ -f "$filename" ]
then
    echo "Regular file"
    wc -l "$filename"
elif [ -d "$filename" ]
then
    echo "It is a directory"
else
    echo "Does not exist"
fi
```

**Q23. Find the largest of three numbers**

```bash
read -p "Enter first number: " num1
read -p "Enter second number: " num2
read -p "Enter third number: " num3

if [ $num1 -gt $num2 ] && [ $num1 -gt $num3 ]
then
    echo "Largest = $num1"
elif [ $num2 -gt $num1 ] && [ $num2 -gt $num3 ]
then
    echo "Largest = $num2"
else
    echo "Largest = $num3"
fi
```

**Q24. SOC failed-login search**

```bash
read -p "Enter your IP address: " ip

if [ -f auth.log ]
then
    echo "File exists"
    grep -i "$ip" auth.log >> failed_logins.txt
else
    echo "File not found"
fi
```

