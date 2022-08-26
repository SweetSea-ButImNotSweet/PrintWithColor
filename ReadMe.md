# **PrintWithColor**

Một wrapper nhỏ nhắn xinh xắn dùng để buff lệnh print() bằng cách thêm tính năng bôi màu cho chữ<br>Đảm bảo mấy đứa newbie Python nhìn xong làm thử báo lỗi tè le sẽ bái phục bạn :>>><br>(Yên tâm, cả PrintWithColor và colorama đều viết bằng Python hết, không có chuyện gọi CPython làm vỡ tương thích đâu!)

# **NẠP THƯ VIỆN VÀO**
Có 2 cách để nạp vào nhé :> tuỳ bạn chọn


```python
''' NOTE: Luôn luôn dòng đầu tiên phải là'''
import PrintWithColor

'''Lý do cho việc này là PrintWithColor có vài thứ bạn có thể chỉnh, và dùng để nạp các thiết lập mặc định, chút nữa mình sẽ nhắc sau'''
```


```python
''' 1.  Không ghi đè lệnh print() của Python '''
from PrintWithColor import printc

'''
Hãy dùng nó khi:
    Cần giữ lệnh print gốc của Python, nếu printc có lỗi bạn có thể thế tạm print() để chữa cháy
'''
```


```python
''' 2.  Ghi đè lệnh print() của Python '''  # Khuyên dùng cách này hơn, từ bước 2 mình sẽ viết ví dụ khi dùng cách 2
                                            # Nếu chọn cách 1 thì khi chép hướng dẫn ở đây hãy thêm chữ c sau chữ print() nhé :>
from PrintWithColor import printc as print

'''
Hãy dùng nó khi
    Bạn không muốn giữ lại lệnh print(), vì đằng nào mình viết để đảm bảo các lệnh dùng print gốc cũng không bị làm sao cả
    Lưu ý: nhớ xoá toàn bộ đối số màu trong lệnh print() đi nhé nếu không cần thư viện PrintWithColor
'''
```

# **CÚ PHÁP**
Gần y chang lệnh print gốc luôn nhé <br> Nhưng sẽ có một chút khác biệt vì **NÓ ĐƯỢC HỖ TRỢ MÀU SẮC!** 

### **CÚ PHÁP của PrintWithColor**


```python
'''print(textfrominput = 'Nội dung, có thể dùng nhiều đối số', sep='Dấu phân cách các đối số', end = 'Dấu kết thúc văn bản của lệnh print'
        file = None, flush = False, f = "Màu chữ", b = "màu nền, s = kiểu màu chữ)'''


import PrintWithColor
from PrintWithColor import printc as print

'''Đây là một ví dụ'''
print("Xin chào!", "Đây là một dòng chữ màu xanh xanh", sep = '\n', f = 'green') # Ở trong Jupyter bạn sẽ không nhìn thấy màu xanh đâu :/
```

### Đối số trong lệnh print() **của Python**

| Đối số        | Mô tả                                                                                   | Mặc định |
|---------------|-----------------------------------------------------------------------------------------|----------|
| textfrominput | Nội dung bạn muốn gõ để hiện thỉ theo mặc định, cho phép sử dụng nhiều đối số           | Bất kỳ   |
| sep           | Là dấu phân cách giữa các đối số (nếu chỉ có 1 đối số textfrominput thì ko có tác dụng) | ' '      |
| end           | Kí tự kết thúc, chỉ tác dụng khi có 1 đối số/tới đối số cuối cùng của textfrominput     | '\n'     |
| file          | Nơi xuất màn hình, trong wrapper này sẽ sử dụng proxy object từ colorama<br>Lưu ý là nếu đối số file là một tệp viết được, theo như lệnh print() gốc, máy sẽ viết ra tệp. Nếu có tệp mà không viết được thì sẽ __báo lỗi__ [1] | None      |
| flush         | Có dọn bộ đệm khi in kết quả không                                                      | False    |

### Đối số trong lệnh print() **của PrintWithColor**

| Đối số        | Mô tả                                                                                   | Mặc định |
|---------------|-----------------------------------------------------------------------------------------|----------|
| textfrominput | Nội dung bạn muốn gõ để hiện thỉ theo mặc định, cho phép sử dụng nhiều đối số           | Bất kỳ   |
| sep           | Là dấu phân cách giữa các đối số (nếu chỉ có 1 đối số textfrominput thì ko có tác dụng) | ' '      |
| end           | Kí tự kết thúc, chỉ tác dụng khi có 1 đối số/tới đối số cuối cùng của textfrominput     | '\n'     |
| file          | Nơi xuất màn hình, trong wrapper này sẽ sử dụng proxy object từ colorama<br>Lưu ý là nếu đối số file là một tệp viết được, theo như lệnh print() gốc, máy sẽ viết ra tệp. Nếu có tệp mà không viết được thì sẽ __vẫn in ra trên màn hình__ [1] | None      |
| flush         | Có dọn bộ đệm khi in kết quả không                                                      | False    |
||||
| f             | Màu của chữ [2] [3]                                                                     | WHITE    |
| b             | Màu của nền chữ [2] [3]                                                                 | BLACK    |
| s             | Kiểu màu của chữ [2] [4]                                                                | NORMAL   |

> **GHI CHÚ**

1. Đối với print() gốc của Python, nếu đối số file là tệp không viết được, Python sẽ báo lỗi. Còn PrintWithColor sẽ bỏ qua và trực tiếp in trên màn hình <BR>
2. Bạn được quyền viết màu bằng chữ hoa/thường cũng chấp nhận nhé
3. Các dải màu được chấp nhận là ['WHITE', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'BLACK']
4. Các kiểu màu được chấp nhận là ['NORMAL', 'DIM', 'BRIGHT']


> **LƯU Ý!**    WINDOWS SẼ __**KHÔNG**__ HIỂN THỊ CHÍNH XÁC MÀU TỐI (DIM) VÀ MÀU BÌNH THƯỜNG (NORMAL) <BR> NÊN HẦU NHƯ BẠN SẼ KHÔNG NHÌN THẤY RÕ SỰ KHÁC BIỆT

# **CÁC THIẾT LẬP BỔ SUNG**

> **LƯU Ý**: Nếu một trong các thiết lập này bị sai, chúng sẽ bị trả giá trị về mặc định của wrapper!!!

## **1.** PrintWithColor.**DoNotResetColor**


```python
import PrintWithColor
from PrintWithColor import printc as print

PrintWithColor.DoNotResetColor = False

print("Đây là một dòng chữ màu xanh lục", f = 'green')
print("Nếu không để máy tự khôi phục màu mặc định, ok, chúng ta sẽ có chữ này màu xanh lục!")

print("")
```

# SỬA LỖI TỪ JUPYTER
**(chỉ áp dụng cho Visual Studio Code)**

## **1. SỬA LỖI KHÔNG THỂ IMPORT MODULE TÙY CHỈNH**

Có một số trường hợp các bạn không chạy code được, báo lỗi import tào lao bí đao
Mình xin bày cách xử lí lỗi:
   
Tiện luôn mình tìm thấy câu trả lời ở đây, bạn có thể xem:
https://stackoverflow.com/questions/58099362/fail-to-use-imports-in-jupyter-notebook-in-vscode 
   
Việc này có thể giúp bạn tiết kiệm hàng giờ lướt Google tìm cách fix :>

Thêm dòng này vào file settings.json
Hướng dẫn: bấm tổ hợp Ctrl+Shift+P, gõ user settings json và nhấn Enter
Thêm dấu , vào dòng mà bên trên cái dấu } ở cuối file
Sau đó xuống dòng và chép dòng này vô
    
    "jupyter.notebookFileRoot": "${workspaceFolder}",

Cuối cùng nhấn Ctrl+S và đóng file đó đi
Nhấn Ctrl+Shift+P và gõ notebook restart và nhấn Enter
Rồi chạy lại code là hết

Chúc các bạn thành công
