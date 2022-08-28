# **PrintWithColor**

Một wrapper nhỏ nhắn xinh xắn dùng để buff cú pháp print() bằng cách thêm tính năng tô màu cho chữ

# **Cách cài đặt**
Để cài qua thư viện PyPi, hãy gõ

```python
pip install PrintWithColor
```
> Đối với những bạn tự hỏi tại sao mình không đặt kí tự \$ trước lệnh như bao dự án khác, cái gì cũng có lý do và nó đây:
> Bởi vì nếu bạn ***quên*** **XOÁ** ***ký tự $ bị thừa*** trong khi dán lệnh sẽ dẫn đến lệnh **bị lỗi!**, chứ còn sao nữa.

# **Cách sử dụng**
Đây là cách sử dụng cơ bản của **PrintWithColor**

```python
from PrintWithColor import printc as print
print('Hello, I am a green line!', f = 'green', b= 'black')
print('Or a line with a cyan background', f = 'black', b = 'cyan')
```

### Đối số trong lệnh print() **của Python**

| Đối số        | Mô tả                                                                                                                                                                                                           | Mặc định |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| textfrominput | Nội dung bạn muốn hiển thị trên màn hình, cho phép bạn sử dụng nhiều đối số                                                                                                                                     | Bất kỳ   |
| sep           | Là dấu phân cách giữa các đối số (nếu chỉ có 1 đối số textfrominput thì ko có tác dụng)                                                                                                                         | ' '      |
| end           | Kí tự kết thúc, chỉ tác dụng khi có 1 đối số/tới đối số cuối cùng của textfrominput                                                                                                                             | '\n'     |
| file          | Nơi xuất màn hình, trong Python mặc định sẽ là sys.stderr<br>Lưu ý là nếu đối số file là một tệp viết được, theo như lệnh print() gốc, máy sẽ viết ra tệp. Nếu có tệp mà không viết được thì sẽ __báo lỗi__ [1] | None     |
| flush         | Có dọn bộ đệm khi in kết quả không                                                                                                                                                                              | False    |

### Đối số trong lệnh print() **của PrintWithColor**

| Đối số        | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Mặc định |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| textfrominput | Nội dung bạn muốn gõ để hiện thỉ theo mặc định, cho phép sử dụng nhiều đối số                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Bất kỳ   |
| sep           | Là dấu phân cách giữa các đối số trong textfrominput (nếu chỉ có 1 đối số textfrominput thì không có tác dụng)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ' '      |
| end           | Kí tự kết thúc, chỉ tác dụng khi có 1 đối số hoặc tới đối số cuối cùng của textfrominput thì nó mới xuất hiện                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | '\n'     |
| file          | Văn bản nên xuất hiện chỗ nào<br>Wrapper này sẽ sử dụng proxy object từ colorama theo mặc định<br><br>Nếu đối số file là một tệp viết được, PrintWithColor sẽ đơn giản là viết file ***như cách cú pháp print() của Python xử lý***.<br><br> Nếu đối số file là tệp không viết được (chỉ đọc) thì sẽ __dựng dưng bỏ qua tệp__, và thay vào đó, PrintWithColor sẽ __in ra trên màn hình__ [1]<br><br>Bạn cũng cần nhớ rằng: đối số này sẽ __bỏ qua__ ***các đối tượng khác trừ một tệp có thể viết được*** (Bởi wrapper này được viết để chạy trên nhiều nền tảng, mình sẽ dùng object proxy từ thư viện Colorama để tránh lỗi không mong muốn!) | None     |
| flush         | Có dọn bộ đệm sau khi in kết quả? không                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | False    |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |          |
| f             | Màu của chữ [2] [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | WHITE    |
| b             | Màu của nền chữ [2] [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | BLACK    |
| s             | Kiểu màu của chữ [2] [4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | NORMAL   |

> **GHI CHÚ**

1. Đối với print() gốc của Python, nếu đối số file là tệp không viết được, Python sẽ tạo ra một ngoại lệ. Còn PrintWithColor sẽ bỏ qua và trực tiếp in trên màn hình
2. Bạn đó thể viết màu bằng chữ hoa/thường cũng chấp nhận nhé
3. Các dải màu được chấp nhận là ['WHITE', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'BLACK']
4. Các kiểu màu được chấp nhận là ['NORMAL', 'DIM', 'BRIGHT']


> **CẢNH BÁO!** Windows sẽ __**KHÔNG**__ hiển thị chính xác màu tối (dim) và màu bình thường (normal). Cho nên trong đa số trường hợp, bạn sẽ không nhìn thấy rõ sự khác biệt <br> (**Đừng có đổ tội lên mình hoặc là tác giả của Colorama**, bởi vì __Windows không hỗ trợ__ ***mã ANSI cho văn bản có màu tối***):cry:<br>**Để biết thêm thông tin**, xui vui lòng truy cập vào cuối đoạn mô tả của Colorama: https://github.com/tartley/colorama#description

# **Các thiết lập đi kèm với cú pháp này**

> **LƯU Ý**: Nếu một trong các thiết lập này bị sai, chúng sẽ bị trả giá trị về **MẶC ĐỊNH** của thiết lập đó<br>**CÁCH SỬA THIẾT LẬP:** sử dụng cú pháp print.change_settings(), **ngoại trừ clear_settings()**

## **1. DoNotResetColor** (Không đặt lại màu về giá trị mặc định)

> **Tác dụng:** Không reset lại màu sau khi chạy xong lệnh print()<br>
> **Giá trị mặc định:** False **(boolean)**<br>
> **Các giá trị được đồng ý:** True, False **(boolean)**

```python
print.change_settings(1, True)
# Hoặc là
print.change_settings('DoNotResetColor', True)
# đều như nhau

# Khi dùng
print('Dòng 1', f='black', b='green')
print('Dòng 2 thế nào cũng phải dùng màu từ lệnh print trước!')
```

## **2. DefaultForegroundColor** (Chỉnh giá trị màu chữ mặc định)

> **Tác dụng:** Thay đổi màu chữ mặc định (khi dùng xong lệnh print mà **DoNotResetColor = False** thì lệnh print tiếp theo sẽ dùng màu do bạn chỉ định!) <br>
> **Giá trị mặc định:** WHITE **(string)** <br>
> **Các giá trị được đồng ý:** WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK **(string)**


```python
print.change_settings(2, 'GREEN')
# Hoặc là
print.change_settings('DefaultForegroundColor', 'GREEN')
# đều như nhau

# Khi sử dụng
print('Chữ màu xanh lục ở đây nhé! Bạn thấy đấy, mình chưa cho đối số f vào lệnh này cả!')
```

## **3. DefaultBackgroundColor** (Chỉnh giá trị màu nền mặc định)

> **Tác dụng:** Thay đổi màu nền mặc định (khi dùng xong lệnh print mà **DoNotResetColor = False** thì lệnh print tiếp theo sẽ dùng màu do bạn chỉ định!) <br>
> **Giá trị mặc định:** BLACK **(string)**<br>
> **Các giá trị được đồng ý:** WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK


```python
print.change_settings(3, 'GREEN')
# Hoặc là
print.change_settings('DefaultBackgroundColor', 'GREEN')
# đều như nhau

# Khi sử dụng
print('Nền màu xanh lục ở đây nhé! Bạn thấy đấy, mình chưa cho đối số b vào lệnh này cả!')
```

## **4. DefaultStyle** (Chỉnh giá trị kiểu màu chữ mặc định)

> **Tác dụng:** Thay đổi kiểu màu chữ mặc định (khi dùng xong lệnh print mà **DoNotResetColor = False** thì lệnh print tiếp theo sẽ dùng kiểu màu chữ do bạn chỉ định!)<br>
> **Giá trị mặc định:** NORMAL **(string)**<br>
> **Các giá trị được đồng ý:** NORMAL, BRIGHT, DIM **(string)**


```python
print.change_settings(4, 'NORMAL')
# Hoặc là
print.change_settings('DefaultStyle', 'NORMAL')
# đều như nhau

# Ví dụ
# Example
print.change_settings('DefaultStyle', 'NORMAL')
print.change_settings('DoNotResetColor', 'True')

print('Dòng 1 có chữ tô màu xanh lục bình thường'), f='green')
print('Nhưng dòng này thì lại có chữ sáng hơn bình thường!', s='bright') 
```

## **5. clear_settings()** (Đặt toàn bộ giá trị về mặc định)

> **Tác dụng:** Xoá toàn bộ cài đặt của PrintWithColor<br>
> **KHÔNG CÓ ĐỐI SỐ & KHÔNG CẢNH BÁO & KHÔNG CÓ GÌ XUẤT RA MÀN HÌNH!**


```python
print.clear_settings()
```
