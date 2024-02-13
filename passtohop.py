# Import các thư viện cần thiết
import itertools
import time
from colorama import Fore, init
import datetime
import os

# Khởi tạo colorama
init(autoreset=True)

# Định nghĩa hàm để tính toán và hiển thị hoán vị
def calculate_permutations():
    last_color = None
    while True:
        # Xóa màn hình trước khi bắt đầu lại chương trình
        os.system('cls' if os.name == 'nt' else 'clear')  
        
        # Nhận đầu vào từ người dùng
        characters = list(input("Nhập vào các ký tự: "))
        
        # Hỏi người dùng cần bao nhiêu kết quả hoán vị
        while True:
            num_permutations = input("Bạn muốn hiển thị bao nhiêu kết quả hoán vị? (để trống để hiển thị tất cả): ")
            if num_permutations == '':
                num_permutations = None
                break
            elif num_permutations.isdigit():
                num_permutations = int(num_permutations)
                break
            else:
                print("Lỗi: Vui lòng nhập một số nguyên hoặc để trống.")
        
        # Tính toán tất cả các hoán vị
        permutations = list(itertools.permutations(characters))[:num_permutations]
        
        # Hiển thị tất cả các hoán vị
        for p in permutations:
            print(' '.join(p))
        
        # Hiển thị tổng số hoán vị
        print("Có tất cả {} hoán vị.".format(len(permutations)))
        
        # Hỏi người dùng có muốn xuất ra file *.txt không
        export_choice = input("Bạn có muốn xuất ra kết quả trên qua file *.txt không? (y/n): ")
        if export_choice.lower() == 'y':
            # Hỏi người dùng đặt tên file
            file_name = input("Nhập tên file bạn muốn lưu (không cần phần mở rộng .txt): ")
            if file_name == '':
                file_name = 'permutations'
            # Thêm thời gian hiện tại vào tên file để tạo tên file duy nhất
            file_name = '{}_{}'.format(file_name, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
            
            # Hỏi người dùng đường dẫn tùy chỉnh
            custom_path_choice = input("Bạn có muốn lưu file vào một đường dẫn tùy chỉnh không? (y/n): ")
            if custom_path_choice.lower() == 'y':
                file_path = input("Nhập đường dẫn bạn muốn lưu file: ")
            else:
                # Xác định đường dẫn đến thư mục Documents
                documents_path = os.path.expanduser('~/Documents')
                # Kiểm tra xem thư mục Documents có tồn tại không, nếu không thì tạo thư mục
                if not os.path.exists(documents_path):
                    os.makedirs(documents_path)
                file_path = os.path.join(documents_path, '{}.txt'.format(file_name))
            
            with open(file_path, 'w') as f:
                for p in permutations:
                    f.write(' '.join(p) + '\n')
            print("Kết quả đã được lưu vào file tại đường dẫn: {}".format(file_path))
        
        # Hỏi người dùng có muốn tiếp tục không
        choice = input("Bạn có muốn tiếp tục không? (y/n): ")
        
        # Nếu người dùng không muốn tiếp tục
        if choice.lower() != 'y':
            # Bắt đầu đếm thời gian
            start_time = time.time()
            
            # Định nghĩa danh sách các màu sắc
            colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
            
            # Hiển thị màu sắc khác nhau trong vòng 2 giây
            while time.time() - start_time < 2:  
                for color in colors:
                    # Nếu đã trôi qua 2 giây, thoát khỏi vòng lặp
                    if time.time() - start_time >= 2:
                        break
                    
                    # Kiểm tra xem màu sắc hiện tại có trùng với màu sắc cuối cùng đã sử dụng không
                    if color == last_color:
                        continue
                    
                    # Xóa màn hình sau mỗi lần in
                    os.system('cls' if os.name == 'nt' else 'clear')  
                    
                    # In ra dòng chữ với màu sắc hiện tại
                    print(color + "Tạm biệt, hẹn lần sau!")
                    
                    # Cập nhật màu sắc cuối cùng đã sử dụng
                    last_color = color
                    
                    # Dừng chương trình trong 0.2 giây
                    time.sleep(0.2)
            
            # Xóa màn hình trước khi in ra dòng chữ cuối cùng
            os.system('cls' if os.name == 'nt' else 'clear')  
            
            # In ra dòng chữ với màu trắng cuối cùng và giữ nó hiển thị trong 5 giây
            print(Fore.WHITE + "Tạm biệt, hẹn lần sau!")  
            time.sleep(5)
            
            # Xóa màn hình sau khi hiển thị dòng chữ cuối cùng
            os.system('cls' if os.name == 'nt' else 'clear')  
            
            # Kết thúc vòng lặp
            break

# Gọi hàm để bắt đầu chương trình
calculate_permutations()
