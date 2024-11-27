from entity import Entity
class NhanVien(Entity):
    def __init__(self, ma="", ten="", viTri="", maDuAn=""):
        super().__init__(ma, ten)
        self.ma = ma
        self.ten = ten
        self.viTri = viTri
        self.maDuAn= maDuAn
    def nhapThongTin(self, maDuAn):
        self.maDuAn = maDuAn
        print("=== Nhập thông tin nhân viên ===")
        ma = qlnv.maTuSinh()
        self.ma= ma
        # self.ma=input("Mã nhân viên: ")
        self.ten=input("Tên nhân viên: ")
        self.viTri=input("Loại vị trí: ")
        if(
            self.ten!=''
            and self.viTri!=''
        ):
            print('Nhập Thông tin nhân viên thành công')
            print('Thông tin nhân viên mới:')
            print(f'Mã nhân viên: {self.ma}')
            print(f'Tên nhân viên: {self.ten}')
            print(f'vị trí: {self.viTri}')
        else:
            while (True):
                check = True
                if (self.ma == ''):
                    check = False
                    self.ma = input('Mã nhân viên: ')
                else:
                    print(f'Mã nhân viên: {self.ma}')
                if (self.ten == ''):
                    check = False
                    self.ten = input('Tên nhân viên: ')
                else:
                    print(f'Tên nhân viên: {self.ten}')
                if (self.viTri == ''):
                    check = False
                    self.viTri = input('vị trí: ')
                else:
                    print(f'vị trí: {self.viTri}')
                if(
                self.ten!=''
                and self.viTri!=''
                ):
                    print('Nhập Thông tin nhân viên thành công')
                    print('Thông tin nhân viên mới:')
                    print(f'Mã nhân viên: {self.ma}')
                    print(f'Tên nhân viên: {self.ten}')
                    print(f'vị trí: {self.viTri}')
                    break
        while(True):
            print('')
            print('00.Quay lại')
            op=input('Nhập lựa chọn của bạn: ')
            if (op=="00"):
                break
            else:
                print('Thông tin nhân viên mới:')
                print(f'Mã nhân viên: {self.ma}')
                print(f'Tên nhân viên: {self.ten}')
                print(f'vị trí: {self.viTri}')
                print('Lựa chọn không hợp lệ')
    def toString(self):
        return f"{self.ma}\t{self.ten}\t{self.viTri}\t{self.maDuAn}"

class QLNhanVien:
    def __init__(self, file_path):
            self.Danh_Sach = list()
            self.file_path =file_path
    def read_from_File(self):
       file = open(self.file_path,'r', encoding='utf-8')
       Lines = file.readlines()
       file.close()
       self.Danh_Sach  = list()
       for nv in Lines:
           tmp=nv.split('\t')
           if (len(tmp)==4):
                dn = NhanVien(tmp[0],tmp[1],tmp[2],tmp[3])
                self.Danh_Sach.append(dn)
    def write2File(self):
            file = open(self.file_path, 'w', encoding='utf-8')
            for i in range(len(self.Danh_Sach )):
                    file.write(self.Danh_Sach[i].toString())
                    file. write ('\n')
            file.close()
    def maTuSinh(self,length=3):
        import random
        string = '0123456789qwertyuiopasdfghjklzxcvbnm'
        while(True):
            code = ''.join(random.choice(string) for _ in range(length))
            ma = 'NV_'+ code
            if( ma != nv.ma for nv in self.Danh_Sach):
                break
        return ma
    def them(self, maDuAn):
            print('')
            print('=== Thêm nhân viên mới===')
            nv = NhanVien()
            nv.nhapThongTin(maDuAn= maDuAn)
            self.Danh_Sach.append(nv)
            file = open(self.file_path, 'a', encoding='utf-8')
            file.write('\n'+nv.toString())
            file.close()
            # self.hienThi(maDuAn)
    def suaThongTin(self, ma=None, ten=None, viTri =None, maDuAn=None):
        for (i, nv) in enumerate(self.Danh_Sach):
            if ((nv.ma == ma) and (nv.maDuAn == maDuAn)):
                nv.ten = ten
                nv.viTri = viTri
                self.write2File()
                print('Sửa thông tin thành công.')
            else:
                print('Sửa thông tin không thành công.')
    def xoa(self, ma):
        xoa = 0
        for (i, nv) in enumerate(self.Danh_Sach):
            if (nv.ma == ma):
                self.Danh_Sach.remove(nv)
                xoa = 1
        # self.hienThi()
        if (xoa == 1):
              print('=== Xoá nhân viên thành công ===')
              self.write2File()
        else:
              print('=== Xoá nhân viên không thành công ===')
    def timKiem(self,maDuAn='', ma='', ten=''):
        print('')
        print('=== Danh sách nhân viên ===')
        maxstrma = max(len(da.ma) for da in self.Danh_Sach)
        if (maxstrma < len('Mã nhân viên')):
            maxstrma = len('Mã nhân viên')
        maxstrten = max(len(da.ten) for da in self.Danh_Sach)
        if (maxstrten < len('Tên nhân viên')):
            maxstrten = len('Tên nhân viên')
        maxstrviTri = max(len(da.viTri) for da in self.Danh_Sach)
        if (maxstrviTri < len('Vị trí')):
            maxstrviTri = len('Vị trí')
        headerformat = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrviTri}}} "
        print(headerformat.format("STT", "Mã nhân viên", "Tên nhân viên", "Vị trí"))
        sl = 0
        for (i, nv) in enumerate(self.Danh_Sach):
            if (nv.ma.strip().lower().__contains__(ma.strip().lower())# contains = in
                    or nv.ten.lower().__contains__(ten.lower())
                    and nv.maDuAn== maDuAn):
                sl = sl + 1
                row_format = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrviTri}}} "
                print(row_format.format(sl, nv.ma, nv.ten, nv.viTri))
        if (sl == 0):
            print("Không có nhân viên nào thoả mãn yêu cầu tìm kiếm")
    def hienThi(self, ma):
        print('')
        print('=== Danh sách nhân viên ===')
        maxstrma = max(len(da.ma) for da in self.Danh_Sach)
        if (maxstrma < len('Mã nhân viên')):
            maxstrma = len('Mã nhân viên')
        maxstrten = max(len(da.ten) for da in self.Danh_Sach)
        if (maxstrten < len('Tên nhân viên')):
            maxstrten = len('Tên nhân viên')
        maxstrviTri = max(len(da.viTri) for da in self.Danh_Sach)
        if (maxstrviTri < len('Vị trí')):
            maxstrviTri = len('Vị trí')
        headerformat = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrviTri}}} "
        print(headerformat.format("STT", "Mã nhân viên", "Tên nhân viên", "Vị trí"))
        # for i, nv in enumerate(self.Danh_Sach):
        #     row_format = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrviTri}}} "
        #     print(row_format.format(i + 1, nv.ma, nv.ten, nv.viTri))
        # ================================
        # print('STT\tMã nhân viên\tTên nhân viên\tVị trí')
        sl = 0
        for (i, nv) in enumerate(self.Danh_Sach):
            if (nv.maDuAn.strip() == ma.strip()):
                sl = sl + 1
                row_format = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrviTri}}} "
                print(row_format.format(sl, nv.ma, nv.ten, nv.viTri))
        if (sl == 0):
            print("Không có nhân viên nào thoả mãn yêu cầu tìm kiếm")

qlnv = QLNhanVien('NhanVien.txt')
qlnv.read_from_File()
class MainNV:
    def them(ma):
          qlnv.them(maDuAn=ma)
    def sua(maDuAn):
        print('')
        qlnv.hienThi(ma=maDuAn)
        print('=== Sửa thông tin ===')
        # ma= input('Nhập mã nhân viên: ')
        while(True):
            ma= input('Nhập mã nhân viên: NV_')
            if(ma!=''):
                ma = 'NV_'+ma
                break
        qlnv.timKiem(str(ma),'###')
        print('Nhập thông tin chỉnh sửa(Không sửa để trống)')
        ten = input('Tên nhân viên: ')
        vitri = input('Vị trí: ')
        for (i, nv) in enumerate(qlnv.Danh_Sach):
            if (nv.ma == ma):
                if(ten==''):
                    ten=nv.ten
                if(vitri==''):
                    vitri = nv.viTri
        qlnv.suaThongTin(str(ma), str(ten), str(vitri), str(maDuAn))
        qlnv.timKiem(maDuAn,str(ma),'###')
    def xoa(maDuAn):
        # qlnv.hienThi()
        
        # ma=input('Nhập mã nhân viên: ')
        while(True):
            print('')
            qlnv.hienThi(ma=maDuAn)
            print('=== Xoá nhân viên ===')
            ma= input('Nhập mã nhân viên: NV_')
            if(ma!=''):
                ma = 'NV_'+ma
                break
        qlnv.timKiem(maDuAn, ma,'###')
        while(True):
            print('Bạn có chắc chắn muốn xoá?')
            print('1.Yes')
            print('2.No')
            ip = input('Nhập lựa chọn: ')
            if (ip=='1'):
                qlnv.xoa(str(ma))
                break
            elif(ip=='2'):
                # fix
                from MQuanLyDuAn import call
                tn = call
                tn.NVmain(maDuAn=maDuAn)
            else:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại!!!')
    def timkiem(maDuAn):
        # nv=input('Nhập mã nhân viên hoặc tên nhân viên: ')
        while(True):
            print('')
            qlnv.hienThi(ma=maDuAn)
            print('=== Tìm kiếm nhân viên ===')
            nv=input('Nhập mã nhân viên hoặc tên nhân viên: ')
            if(nv!=''):
                break
        qlnv.timKiem(maDuAn, str(nv), str(nv))
    def hienthi(ma):
         qlnv.hienThi(ma=ma)

# nv = QLNhanVien('NhanVien.txt')
# nv.read_from_File()
# nv.them('w')
# nv.hienThi('w')
# mnv = MainNV
# mnv.hienthi(ma='w')









