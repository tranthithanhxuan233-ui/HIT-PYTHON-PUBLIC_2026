## Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

- **Python là ngôn ngữ thông dịch (interpreted language).**
- **Tại sao?**
  Mã nguồn Python không được biên dịch trực tiếp toàn bộ thành mã máy (machine code) giống như các ngôn ngữ C hay C++ để phần cứng thực thi trực tiếp. Thay vào đó, mã nguồn (mã mà chúng ta viết) sẽ được xử lý qua hai bước:
  1. Đầu tiên, mã nguồn được biên dịch (compile) ngầm thành một dạng mã trung gian gọi là **bytecode** (thường được lưu dưới định dạng `.pyc`).
  2. Tiếp theo, bytecode này sẽ được một máy ảo gọi là **Python Virtual Machine (PVM)** đọc và thông dịch (interpret) từng dòng lệnh một để thực thi.
  
  Mặc dù có bước biên dịch ngầm ra bytecode, nhưng bởi vì chương trình được chạy qua trình thông dịch (interpreter) thay vì tạo ra file thực thi mã máy trực tiếp và người lập trình không cần gọi một quy trình biên dịch riêng biệt, nên Python được phân loại rộng rãi là ngôn ngữ thông dịch.

---

## Bài 2: Liệt kê

### Các kiểu dữ liệu cơ bản trong Python:
- **Kiểu số (Numeric):**
  - `int`: Số nguyên 
  - `float`: Số thực 
  - `complex`: Số phức 
- **Kiểu chuỗi (Text/String):** 
  - `str`: Chuỗi ký tự (ví dụ: `"Hello"`, `'Python'`)
- **Kiểu chuỗi/tập hợp theo thứ tự (Sequence):**
  - `list`: Danh sách, có thể thay đổi (ví dụ: `[1, 2, "a"]`)
  - `tuple`: Tuple, tương tự list nhưng không thể thay đổi sau khi tạo (ví dụ: `(1, 2, 3)`)
  - `range`: Dãy số (thường dùng trong vòng lặp)
- **Kiểu ánh xạ (Mapping):**
  - `dict`: Từ điển lưu trữ theo cặp key-value (ví dụ: `{"name": "John", "age": 20}`)
- **Kiểu tập hợp (Set):**
  - `set`: Tập hợp các phần tử duy nhất, không có thứ tự
  - `frozenset`: Giống set nhưng không thể thay đổi
- **Kiểu Boolean:** 
  - `bool`: Lưu trữ giá trị đúng/sai (`True` hoặc `False`)
- **Kiểu None:** 
  - `NoneType`: Biểu diễn giá trị rỗng hoặc không có giá trị (`None`)

### Các toán tử trong Python:
- **Toán tử số học (Arithmetic operators):** `+` (cộng), `-` (trừ), `*` (nhân), `/` (chia), `//` (chia lấy phần nguyên), `%` (chia lấy phần dư), `**` (lũy thừa).
- **Toán tử gán (Assignment operators):** `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, ...
- **Toán tử so sánh (Comparison operators):** `==` (bằng), `!=` (khác), `>` (lớn hơn), `<` (nhỏ hơn), `>=` (lớn hơn hoặc bằng), `<=` (nhỏ hơn hoặc bằng).
- **Toán tử logic (Logical operators):** `and` (và), `or` (hoặc), `not` (phủ định).
- **Toán tử nhận dạng (Identity operators):** `is` (kiểm tra cùng một đối tượng trong bộ nhớ), `is not`.
- **Toán tử thành viên (Membership operators):** `in` (kiểm tra phần tử có nằm trong tập hợp không), `not in`.
- **Toán tử thao tác bit (Bitwise operators):** `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (dịch trái), `>>` (dịch phải).

### Mệnh đề điều kiện và vòng lặp:
- **Mệnh đề điều kiện:**
  - `if`: Nếu điều kiện đúng thì thực thi.
  - `elif`: (Else If) Nếu điều kiện `if` sai thì kiểm tra điều kiện này.
  - `else`: Nếu tất cả các điều kiện trên đều sai thì thực thi.
- **Vòng lặp:**
  - `for`: Lặp qua một tập hợp (như `list`, `string`, `tuple`, `dict`) hoặc một dãy số (`range`).
  - `while`: Lặp liên tục chừng nào điều kiện kiểm tra vẫn còn trả về `True`.
- **Các từ khóa kiểm soát vòng lặp:**
  - `break`: Thoát khỏi vòng lặp ngay lập tức.
  - `continue`: Bỏ qua các lệnh còn lại trong lần lặp hiện tại và chuyển sang lần lặp tiếp theo.
  - `pass`: Lệnh giữ chỗ, không làm gì cả.

### Kiểu dữ liệu True, False:
- Đây là giá trị của kiểu dữ liệu **Boolean** (`bool`).
- Trong Python, giá trị hợp lệ chỉ là `True` (Đúng) hoặc `False` (Sai). Các chữ cái đầu tiên "T" và "F" bắt buộc phải viết hoa.
- Đây thường là kết quả trả về của các phép toán so sánh, toán tử logic và được sử dụng rộng rãi để điều khiển luồng thực thi trong các mệnh đề điều kiện (`if`, `while`).
- Trong các phép toán số học, Python coi `True` tương đương với số nguyên `1` và `False` tương đương với số nguyên `0`.