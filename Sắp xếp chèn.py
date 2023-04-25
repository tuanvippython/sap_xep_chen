# Sử dụng hàm split để nhập dãy số
list = input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()
a = [int(num) for num in list]
print("Dãy số vừa nhập là: ",a)

print("----Dãy số sau khi sắp xếp tăng dần----")

# Sử dụng vòng lặp for với biến i để duyệt qua từng phần tử trong danh sách (chạy từ phần tử thứ 2 đến phần tử cuối cùng)
for i in range(1, len(a)):
    current_value = a[i]
    # j là giá trị đứng trước giá trị hiện tại i
    j = i - 1
    # vòng lặp sẽ kết thúc khi j có giá trị âm 
    while j >= 0 and a[j] > current_value:
        # Thực hiện đổi chỗ 2 giá trị với nhau nếu vị trí thứ j lớn hơn giá trị hiện tại (vị trí được đem ra so sánh)
        a[j + 1] = a[j]
        j = j - 1
    # Gán phần tử hiện tại vào vị trí thích hợp trong dãy
    a[j + 1] = current_value

print(a)

print("----Dãy số sau khi sắp xếp giảm dần----")

# Sử dụng vòng lặp for với biến i để duyệt qua từng phần tử trong danh sách (chạy từ phần tử thứ 2 đến phần tử cuối cùng)
for i in range(1, len(a)):
    current_value = a[i]
    # j là giá trị đứng trước giá trị hiện tại i
    j = i - 1
    # vòng lặp sẽ kết thúc khi j có giá trị âm 
    while j >= 0 and a[j] < current_value:
        # Thực hiện đổi chỗ 2 giá trị với nhau nếu vị trí thứ j nhỏ hơn giá trị hiện tại (vị trí được đem ra so sánh)
        a[j + 1] = a[j]
        j = j - 1
    # Gán phần tử hiện tại vào vị trí thích hợp trong dãy
    a[j + 1] = current_value

print(a)
