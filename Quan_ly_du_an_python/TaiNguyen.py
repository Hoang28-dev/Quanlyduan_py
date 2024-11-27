from entity import Entity
class TaiNguyen(Entity):
    def __init__(self, ma="", ten="", loaiTaiNguyen ="", soLuong="",maDuAn=""):
        super().__init__(ma, ten)
        self.ma = ma
        self.ten = ten
        self.loaiTaiNguyen = loaiTaiNguyen
        self.soLuong = soLuong
        self.maDuAn = maDuAn
    def nhapThongTin(self, maDuAn):
        self.maDuAn = maDuAn
        print("=== Nhập thông tin tài nguyên ===")
        ma = qltn.maTuSinh()
        self.ma=ma
        # self.ma=input("Mã tài nguyên: ")
        self.ten=input("Tên tài nguyên: ")
        self.loaiTaiNguyen=input("Loại tài nguyên: ")
        self.soLuong=input("Số lượng: ")
        if (
            self.ma !='' 
            and self.ten!=''
            and self.loaiTaiNguyen!='' 
            and self.soLuong!=''
            ):
            print('Nhập Thông tin tài nguyên thành công')
            print('')
            print('Thông tin tài nguyên mới:')
            print(f'Mã tài nguyên: {self.ma}')
            print(f'Tên tài nguyên: {self.ten}')
            print(f'Loại tài nguyên: {self.loaiTaiNguyen}')
            print(f'Số lượng: {self.soLuong}')
        else:
            while (True):
                check = True
                if (self.ma == ''):
                    check = False
                    self.ma = input('Mã tài nguyên: ')
                else:
                    print(f'Mã tài nguyên: {self.ma}')
                if (self.ten == ''):
                    check = False
                    self.ten = input('Tên tài nguyên: ')
                else:
                    print(f'Tên tài nguyên: {self.ten}')
                if (self.loaiTaiNguyen == ''):
                    check = False
                    self.loaiTaiNguyen = input('Loại tài nguyên: ')
                else:
                    print(f'Loại tài nguyên: {self.loaiTaiNguyen}')
                if (self.soLuong == ''):
                    check = False
                    self.soLuong = input('Số lượng: ')
                else:
                    print(f'Số lượng: {self.soLuong}')
                if (
                    self.ma !='' 
                    and self.ten!=''
                    and self.loaiTaiNguyen!='' 
                    and self.soLuong!=''
                    ):
                    print('Nhập Thông tin tài nguyên thành công')
                    print('')
                    print('Thông tin tài nguyên mới:')
                    print(f'Mã tài nguyên: {self.ma}')
                    print(f'Tên tài nguyên: {self.ten}')
                    print(f'Loại tài nguyên: {self.loaiTaiNguyen}')
                    print(f'Số lượng: {self.soLuong}')
                    break
        while(True):
            print('')
            print('00.Quay lại')
            op=input('Nhập lựa chọn của bạn: ')
            if (op=="00"):
                break
            else:
                print('')
                print('Thông tin tài nguyên mới:')
                print(f'Mã tài nguyên: {self.ma}')
                print(f'Tên tài nguyên: {self.ten}')
                print(f'Loại tài nguyên: {self.loaiTaiNguyen}')
                print(f'Số lượng: {self.soLuong}')
                print('Lựa chọn không hợp lệ')
    def toString(self):
        return f"{self.ma}\t{self.ten}\t{self.loaiTaiNguyen}\t{self.soLuong}\t{self.maDuAn}"
class QLTaiNguyen:
    def __init__(self, file_path):
            self.Danh_Sach = list()
            self.file_path =file_path
    def read_from_File(self):
       file = open(self.file_path,'r', encoding='utf-8')
       Lines = file.readlines()
       file.close()
       self.Danh_Sach = list()
       for tn in Lines:
           tmp=tn.split('\t')
           if (len(tmp)==5):
                dn = TaiNguyen(tmp[0],tmp[1],tmp[2],tmp[3], tmp[4])
                self.Danh_Sach.append(dn)
    def write2File(self):
            file = open(self.file_path, 'w', encoding='utf-8')
            for i in range(len(self.Danh_Sach )):
                    file.write(self.Danh_Sach [i].toString())
                    file. write ('\n')
            file.close()
    def maTuSinh(self,length=3):
        import random
        string = '0123456789qwertyuiopasdfghjklzxcvbnm'
        while(True):
            code = ''.join(random.choice(string) for _ in range(length))
            ma = 'TN_'+ code
            if( ma != tn.ma for tn in self.Danh_Sach):
                break
        return ma
    def them(self, maDuAn):
            print('')
            print('=== Thêm tài nguyên mới===')
            tn = TaiNguyen()
            tn.nhapThongTin(maDuAn = maDuAn)
            self.Danh_Sach.append(tn)
            file = open(self.file_path, 'a', encoding='utf-8')
            file.write('\n'+tn.toString()) #ghi vào cuối file
            file.close()
    def suaThongTin(self, ma=None, ten=None, loaiTaiNguyen =None, soLuong=None):
        for (i, tn) in enumerate(self.Danh_Sach):
            if (tn.ma == ma):
                tn.ten = ten
                tn.loaiTaiNguyen = loaiTaiNguyen
                tn.soLuong = soLuong
                self.write2File()
                print('Sửa Thông tin thành công.')
            else:
                print('Sửa thông tin không thành công.')
    def xoa(self, ma):
        print('=== Xoá tài nguyên ===')
        xoa = 0
        for (i, tn) in enumerate(self.Danh_Sach):
            if (tn.ma == ma):
                self.Danh_Sach.remove(tn)
                xoa = 1
        # self.hienThi()
        if (xoa == 1):
              print('=== Xoá tài nguyên thành công ===')
              self.write2File()
        else:
              print('=== Xoá tài nguyên không thành công ===')
    def timKiem(self, maDuAn, ma='', ten=''):
        print('=== Danh sách tài nguyên ===')
        maxstrma = max(len(da.ma) for da in self.Danh_Sach)
        if (maxstrma < len('Mã tài nguyên')):
            maxstrma = len('Mã tài nguyên')
        maxstrten = max(len(da.ten) for da in self.Danh_Sach)
        if (maxstrten < len('Tên tài nguyên')):
            maxstrten = len('Tên tài nguyên')
        maxstrloaiTaiNguyen = max(len(da.loaiTaiNguyen) for da in self.Danh_Sach)
        if (maxstrloaiTaiNguyen < len('Loại tài nguyên')):
            maxstrloaiTaiNguyen = len('Loại tài nguyên')
        maxstrsoLuong = max(len(da.soLuong) for da in self.Danh_Sach)
        if (maxstrsoLuong < len('Số lương')):
            maxstrsoLuong = len('Số lương')
        headerformat = f"{{:<3}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrloaiTaiNguyen}}} {{:<{maxstrsoLuong}}} "
        print(headerformat.format("STT", "Mã tài nguyên", "Tên tài nguyên", "Loại tài nguyên", "Số lượng"))
        sl = 0
        for (i, tn) in enumerate(self.Danh_Sach):
            if (tn.ma.lower().__contains__(ma.lower())
                    or tn.ten.lower().__contains__(ten.lower())
                    and tn.maDuAn == maDuAn):
                sl = sl + 1
                row_format = f"{{:<3}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrloaiTaiNguyen}}} {{:<{maxstrsoLuong}}} "
                print(row_format.format(sl, tn.ma, tn.ten, tn.loaiTaiNguyen, tn.soLuong))
        if (sl == 0):
            print("Không có tài nguyên nào thoả mãn yêu cầu tìm kiếm")
    def hienThi(self, ma):
        print('=== Danh sách tài nguyên ===')
        maxstrma = max(len(da.ma) for da in self.Danh_Sach)
        if (maxstrma < len('Mã tài nguyên')):
            maxstrma = len('Mã tài nguyên')
        maxstrten = max(len(da.ten) for da in self.Danh_Sach)
        if (maxstrten < len('Tên tài nguyên')):
            maxstrten = len('Tên tài nguyên')
        maxstrloaiTaiNguyen = max(len(da.loaiTaiNguyen) for da in self.Danh_Sach)
        if (maxstrloaiTaiNguyen < len('Loại tài nguyên')):
            maxstrloaiTaiNguyen = len('Loại tài nguyên')
        maxstrsoLuong = max(len(da.soLuong) for da in self.Danh_Sach)
        if (maxstrsoLuong < len('Số lương')):
            maxstrsoLuong = len('Số lương')
        headerformat = f"{{:<3}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrloaiTaiNguyen}}} {{:<{maxstrsoLuong}}} "
        print(headerformat.format("STT", "Mã tài nguyên", "Tên tài nguyên", "Loại tài nguyên", "Số lượng"))
        # for i, tn in enumerate(self.Danh_Sach):
        #     row_format = f"{{:<3}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrloaiTaiNguyen}}} {{:<{maxstrsoLuong}}} "
        #     print(row_format.format(i + 1, tn.ma, tn.ten, tn.loaiTaiNguyen, tn.soLuong))
        # =============================
        # print('STT\tMã tài nguyên\tTên tài nguyên\tLoại tài nguyên\tSố lượng')
        sl = 0
        for (i, tn) in enumerate(self.Danh_Sach):
            if (tn.maDuAn.strip() == ma.strip()):
                sl = sl + 1
                row_format = f"{{:<3}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrloaiTaiNguyen}}} {{:<{maxstrsoLuong}}} "
                print(row_format.format(sl, tn.ma, tn.ten, tn.loaiTaiNguyen, tn.soLuong))
        if (sl == 0):
            print("Không có tài nguyên nào thoả mãn yêu cầu tìm kiếm")

qltn = QLTaiNguyen('TaiNguyen.txt')
qltn.read_from_File()
class mainTN():
    
    def them(maDuAn):
        qltn.them(maDuAn = maDuAn)
    def sua(maDuAn):
        # ma = input('Nhập mã tài nguyên: ')
        while(True):
            print('')

            print('=== Sửa thông tin tài nguyên ===')
            ma = input('Nhập mã tài nguyên: TN_')
            if(ma!=''):
                ma='TN_' + ma
                break
        qltn.timKiem(maDuAn,str(ma),'###')
        print('Thông tin chỉnh sửa(Không sửa để trống)')
        ten = input('Tên tài nguyên: ')
        loai= input('Loại tài nguyên: ')
        sl = input('Số lượng: ')
        for (i, tn) in enumerate(qltn.Danh_Sach):
            if (tn.ma == ma):
                if (ten==''):
                    ten = tn.ten
                if(loai==''):
                    loai = tn.loaiTaiNguyen 
                if (sl==''):
                    sl= tn.soLuong
        qltn.suaThongTin(str(ma), str(ten), str(loai), str(sl))
        qltn.timKiem(maDuAn,str(ma),'###')
    def xoa(maDuAn):
        
        # qltn.hienThi()
        print('')
        print('=== Xoá tài nguyên ===')
        # ma = input('Nhập mã tài nguyên: ')
        while(True):
            ma = input('Nhập mã tài nguyên: TN_')
            if(ma!=''):
                ma='TN_' + ma
                break
        qltn.timKiem(maDuAn,str(ma),'###')
        while(True):
            print('Bạn có chắc chắn muốn xoá?')
            print('1.Yes')
            print('2.No')
            ip = input('Nhập lựa chọn: ')
            if (ip=='1'):
                qltn.xoa(str(ma))
                break
            elif(ip=='2'):
                # fix
                from MQuanLyDuAn import call
                tn = call
                tn.TNmain(maDuAn=maDuAn)
            else:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại!!!')
    def timkiem(maDuAn):
        print('')
        print('=== Tìm kiếm tài nguyên ===')
        # tt=input('Nhập mã tài nguyên hoặc tên tài nguyên: ')
        while(True):
            tt=input('Nhập mã tài nguyên hoặc tên tài nguyên: ')
            if(tt!=''):
                break
        qltn.timKiem(maDuAn,str(tt), str(tt))
    def hienthi(ma):
        qltn.hienThi( ma = ma)
# qltn.them('b')
# qltn.hienThi(ma='b')
# mai = mainTN
# mai.sua()
# mai.xoa()



