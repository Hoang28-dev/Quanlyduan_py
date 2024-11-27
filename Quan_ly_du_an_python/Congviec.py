from entity import Entity
class CongViec(Entity):
    def __init__(self, ma="", ten="", moTa="", nguoiPhuTrach="", trangThai="", ngayBatDau="", ngayKetThuc="", maDuAn=''):
        super().__init__(ma, ten)
        self.moTa = moTa
        self.nguoiPhuTrach = nguoiPhuTrach  # Đối tượng Employee
        self.trangThai = trangThai  # Ví dụ: 'Đang làm', 'Đã hoàn thành'
        self.ngayBatDau = ngayBatDau  # Ngày bắt đầu thực tế
        self.ngayKetThuc = ngayKetThuc  # Ngày kết thúc thực tế
        self.maDuAn = maDuAn
    def NhapThongTin(self, maDuAn):
        self.maDuAn = maDuAn
        print('=== Nhập thông tin công việc ===')
        ma = qlcv.maTuSinh()
        self.ma = ma
        # self.ma = input('Nhập mã công việc: ')
        self.ten = input('Nhập tên công việc: ')
        self.moTa = input('Mô tả công việc: ')
        self.nguoiPhuTrach = input('Nhập tên người phụ trách : ')  # Đối tượng Employee
        self.ngayBatDau = input('Nhập ngày bắt đầu: ')  # Ngày bắt đầu thực tế
        self.ngayKetThuc = input('Nhập ngày kết thúc:')
        while(True):
            print('Trạng thái công việc(chọn 1-5)')
            print('1.Đang tiến hành')
            print('2.Quá hạn(Chậm tiến độ)')
            print('3.Đã huỷ')
            print('4.Tạm hoãn')
            print('5.Hoàn thành')
            tt = input('Trạng thái công việc: ')
            if (str(tt)=='1'):
                self.trangThai = 'Đang tiến hành'
                break
            elif (str(tt)=='2'):
                self.trangThai = 'Quá hạn(Chậm tiến độ)'
                break
            elif (str(tt)=='3'):
                self.trangThai = 'Đã huỷ'
                break
            elif (str(tt)=='4'):
                self.trangThai = 'Tạm hoãn'
                break
            elif (str(tt)=='5'):
                self.trangThai = 'Hoàn thành'
                break
            else:
                print('Lựa chọn không hợp lệ')
        
        if((self.ma!='') 
        and (self.ten!='') 
        and (self.moTa!='') 
        and (self.ngayBatDau!='') 
        and (self.ngayKetThuc!='')
        and (self.nguoiPhuTrach!='')
        and (self.trangThai!='')):
            print('Nhập thông tin thành công')
            print('')
            print('Thông tin tài nguyên mới:')
            print(f'Mã công việc: {self.ma}')
            print(f'Tên công việc: {self.ten}')
            print(f'Mô tả công việc: {self.moTa}')
            print(f'Người phụ trách: {self.nguoiPhuTrach}')
            print(f'Ngày bắt đầu công việc: {self.ngayBatDau}')
            print(f'Ngày kết thúc công việc: {self.ngayKetThuc}')
            print(f'Tình trạng: {self.trangThai}')
        else:
            while(True):
                    print('')
                    print('Vui lòng nhập đầy đủ thông tin')
                    if (self.ma==''):
                        check=False
                        self.ma = input('Mã công việc:')
                    else:
                        print(f'Mã công việc: {self.ma}')
                    if (self.ten==''):
                        check=False
                        self.ten= input('Tên công việc:')
                    else:
                        print(f'Tên công việc: {self.ten}')
                    if (self.moTa==''):
                        check=False
                        self.moTa = input('Mô tả công việc:')
                    else:
                        print(f'Mô tả công việc: {self.moTa}')
                    if (self.ngayBatDau==''):
                        check=False
                        self.ngayBatDau = input('Ngày bắt đầu công việc:')
                    else:
                        print(f'Ngày bắt đầu công việc: {self.ngayBatDau}')
                    if (self.ngayKetThuc==''):
                        check=False
                        self.ngayKetThuc = input('Ngày kết thúc công việc:')
                    else:
                        print(f'Ngày kết thúc công việc: {self.ngayKetThuc}')
                    if (self.nguoiPhuTrach==''):
                        check=False
                        self.nguoiPhuTrach = input('Tên người phụ trách:')
                    else:
                        print(f'Tên người phụ trách: {self.nguoiPhuTrach}')
                    if(self.trangThai==''
                        and self.trangThai!='1'
                        and self.trangThai!='2'
                        and self.trangThai!='3'
                        and self.trangThai!='4'
                        and self.trangThai!='5'
                        ):
                        print('Trạng thái công việc(chọn 1-5)')
                        print('1.Đang tiến hành')
                        print('2.Quá hạn(Chậm tiến độ)')
                        print('3.Đã huỷ')
                        print('4.Tạm hoãn')
                        print('5.Hoàn thành')
                        tt = input('Trạng thái công việc: ')
                        if (str(tt)=='1'):
                            self.trangThai = 'Đang tiến hành'
                        elif (str(tt)=='2'):
                            self.trangThai = 'Quá hạn(Chậm tiến độ)'
                        elif (str(tt)=='3'):
                            self.trangThai = 'Đã huỷ'
                        elif (str(tt)=='4'):
                            self.trangThai = 'Tạm hoãn'
                        elif (str(tt)=='5'):
                            self.trangThai = 'Hoàn thành'
                        if((self.ma!='') 
                        and (self.ten!='') 
                        and (self.moTa!='') 
                        and (self.ngayBatDau!='') 
                        and (self.ngayKetThuc!='')
                        and (self.nguoiPhuTrach!='')
                        and (self.trangThai!='')):
                            print('Nhập thông tin thành công')
                            print('')
                            print('Thông tin tài nguyên mới:')
                            print(f'Mã công việc: {self.ma}')
                            print(f'Tên công việc: {self.ten}')
                            print(f'Mô tả công việc: {self.moTa}')
                            print(f'Người phụ trách: {self.nguoiPhuTrach}')
                            print(f'Ngày bắt đầu công việc: {self.ngayBatDau}')
                            print(f'Ngày kết thúc công việc: {self.ngayKetThuc}')
                            print(f'Tình trạng: {self.trangThai}')
                            break
        while(True):
            print('')
            print('00.Quay lại')
            op=input('Nhập lựa chọn của bạn: ')
            if (op=="00"):
                break
            else:
                print('Thông tin tài nguyên mới:')
                print(f'Mã công việc: {self.ma}')
                print(f'Tên công việc: {self.ten}')
                print(f'Mô tả công việc: {self.moTa}')
                print(f'Người phụ trách: {self.nguoiPhuTrach}')
                print(f'Ngày bắt đầu công việc: {self.ngayBatDau}')
                print(f'Ngày kết thúc công việc: {self.ngayKetThuc}')
                print(f'Tình trạng: {self.trangThai}')
                print('Lựa chọn không hợp lệ')
    def toString(self):
        return f"{self.ma}\t{self.ten}\t{self.moTa}\t{self.nguoiPhuTrach}\t{self.trangThai}\t{self.ngayBatDau}\t{self.ngayKetThuc}\t{self.maDuAn}"
class QLCongViec:
    def __init__(self, file_path):
          self.Danh_Sach = list()
          self.file_path = file_path
    def read_from_File(self):
        file = open(self.file_path,'r',encoding='utf-8')
        Lines = file.readlines()
        file.close()
        self.Danh_Sach = list()
        for cv in Lines:
            tmp = cv.split('\t')
            if (len(tmp)==8):
               dn = CongViec(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6],tmp[7])
               self.Danh_Sach.append(dn)
    def write2File(self):
        file = open(self.file_path, 'w', encoding='utf-8')
        for i in range(len(self.Danh_Sach)):
            file.write(self.Danh_Sach[i].toString())
            file. write ('\n')
        file.close()
    def maTuSinh(self,length=3):
        import random
        string = '0123456789qwertyuiopasdfghjklzxcvbnm'
        while(True):
            code = ''.join(random.choice(string) for _ in range(length))
            ma = 'DA_'+ code
            if( ma != cv.ma for cv in self.Danh_Sach):
                break
        return ma
    def them(self, maDuAn):
            print('=== Thêm công việc mới ===')
            cv = CongViec()
            cv.NhapThongTin(maDuAn=maDuAn)
            self.Danh_Sach.append(cv)
            file = open(self.file_path, 'a', encoding='utf-8')
            file.write('\n'+cv.toString())
            file.close()
            self.hienThi(maDuAn=maDuAn)
    def suaThongTin(self,ma=None,ten=None,moTa=None,nguoiPhuTrach=None,trangThai=None,ngayBatDau=None,ngayKetThuc=None, maDuAn=None):
        check = False
        for (i, cv) in enumerate(self.Danh_Sach):
            if (cv.ma.strip() == ma.strip() and cv.maDuAn.strip() == maDuAn.strip()):
                cv.ten = ten
                cv.moTa = moTa
                cv.nguoiPhuTrach = nguoiPhuTrach
                cv.trangThai = trangThai
                cv.ngayBatDau = ngayBatDau
                cv.ngayKetThuc = ngayKetThuc
                self.write2File()
                check = True
        if(check ==True):
            print('Sửa Thông tin thành công.')
        else:
            print('Sửa thông tin không thành công.')
    def xoa(self,ma):
       print('===Xóa công việc===')
       xoa = 0
       for (i, cv) in enumerate(self.Danh_Sach):
           if (cv.ma == ma):
              self.Danh_Sach.remove(cv)
              xoa = 1
    #    self.hienThi()
       if (xoa == 1):
             print('== Xóa công việc thành công ===')
             self.write2File()
       else:
             print('== Xóa công việc không thành công ==')
    def timKiem(self,maDuAn='', ma='', ten=''):
        print('')
        print('=== Danh sách công việc ===')
        maxstrma = max(len(cv.ma) for cv in self.Danh_Sach)
        if (maxstrma < len('Mã công việc')):
            maxstrma = len('Mã công việc')
        maxstrten = max(len(cv.ten) for cv in self.Danh_Sach)
        if (maxstrten < len('Tên công việc')):
            maxstrten = len('Tên công việc')
        maxstrmoTa = max(len(cv.moTa) for cv in self.Danh_Sach)
        if (maxstrmoTa < len('Mô tả')):
            maxstrmoTa = len('moTa')
        maxstrnguoiPhuTrach = max(len(cv.nguoiPhuTrach) for cv in self.Danh_Sach)
        if (maxstrnguoiPhuTrach < len('Người phụ trách')):
            maxstrnguoiPhuTrach = len('Người phụ trách')
        maxstrngayBatDau = max(len(cv.ngayBatDau) for cv in self.Danh_Sach)
        if (maxstrngayBatDau < len('Ngày bắt đầu')):
            maxstrngayBatDau = len('Ngày bắt đầu')
        maxstrngayKetThuc = max(len(cv.ngayKetThuc) for cv in self.Danh_Sach)
        if (maxstrngayKetThuc < len('Ngày kết thúc')):
            maxstrngayKetThuc = len('Ngày kết thúc')
        maxstrtrangThai = max(len(cv.trangThai) for cv in self.Danh_Sach)
        if (maxstrtrangThai < len('Trạng thái')):
            maxstrtrangThai = len('Trạng thái')
        headerformat = f"{{:<6}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrmoTa}}} {{:<{maxstrnguoiPhuTrach}}} {{:<{maxstrngayBatDau}}} {{:<{maxstrngayKetThuc}}} {{:<{maxstrtrangThai}}} "
        print(
            headerformat.format("STT", "Mã công việc", "Tên công việc", "Mô tả" ,"Người phụ trách" , "Ngày bắt đầu" , "Ngày kết thúc","Trạng thái"))
        sl = 0
        for (i, cv) in enumerate(self.Danh_Sach):
            if (cv.ma.strip().lower().__contains__(ma.strip().lower())
                    or cv.ten.strip().lower().__contains__(ten.strip().lower())
                    and (cv.maDuAn == maDuAn)):
                sl = sl + 1
                row_format = f"{{:<7}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrmoTa}}} {{:<{maxstrnguoiPhuTrach}}} {{:<{maxstrngayBatDau}}} {{:<{maxstrngayKetThuc}}} {{:<{maxstrtrangThai}}} "
                print(row_format.format(sl, cv.ma, cv.ten, cv.moTa,cv.nguoiPhuTrach,cv.ngayBatDau,cv.ngayKetThuc,cv.trangThai))
        if sl == 0:
            print("Không có công việc nào thoả mãn yêu cầu tìm kiếm")
    def hienThi(self, maDuAn):
        print('=== Danh sách công việc ===')
        maxstrma = max(len(cv.ma) for cv in self.Danh_Sach)
        if (maxstrma < len('Mã công việc')):
            maxstrma = len('Mã công việc')
        maxstrten = max(len(cv.ten) for cv in self.Danh_Sach)
        if (maxstrten < len('Tên công việc')):
            maxstrten = len('Tên công việc')
        maxstrmoTa = max(len(cv.moTa) for cv in self.Danh_Sach)
        if (maxstrmoTa < len('Mô tả')):
            maxstrmoTa = len('moTa')
        maxstrnguoiPhuTrach = max(len(cv.nguoiPhuTrach) for cv in self.Danh_Sach)
        if (maxstrnguoiPhuTrach < len('Người phụ trách')):
            maxstrnguoiPhuTrach = len('Người phụ trách')
        maxstrngayBatDau = max(len(cv.ngayBatDau) for cv in self.Danh_Sach)
        if (maxstrngayBatDau < len('Ngày bắt đầu')):
            maxstrngayBatDau = len('Ngày bắt đầu')
        maxstrngayKetThuc = max(len(cv.ngayKetThuc) for cv in self.Danh_Sach)
        if (maxstrngayKetThuc < len('Ngày kết thúc')):
            maxstrngayKetThuc = len('Ngày kết thúc')
        maxstrtrangThai = max(len(cv.trangThai) for cv in self.Danh_Sach)
        if (maxstrtrangThai < len('Trạng thái')):
            maxstrtrangThai = len('Trạng thái')
        headerformat = f"{{:<6}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrmoTa}}} {{:<{maxstrnguoiPhuTrach}}} {{:<{maxstrngayBatDau}}} {{:<{maxstrngayKetThuc}}} {{:<{maxstrtrangThai}}} "
        print(headerformat.format("STT", "Mã công việc", "Tên công việc", "Mô tả" ,"Người phụ trách" , "Ngày bắt đầu" , "Ngày kết thúc","Trạng thái"))
        sl=0
        for i, cv in enumerate(self.Danh_Sach):
            if(cv.maDuAn.strip() == maDuAn):
                sl=sl+1
                row_format = f"{{:<7}} {{:<{maxstrma}}} {{:<{maxstrten}}} {{:<{maxstrmoTa}}} {{:<{maxstrnguoiPhuTrach}}} {{:<{maxstrngayBatDau}}} {{:<{maxstrngayKetThuc}}} {{:<{maxstrtrangThai}}} "
                print(row_format.format(sl, cv.ma, cv.ten, cv.moTa, cv.nguoiPhuTrach,cv.ngayBatDau,cv.ngayKetThuc,cv.trangThai))
        if sl == 0:
            print("Không có công việc nào thoả mãn yêu cầu tìm kiếm")
qlcv = QLCongViec("CongViec.txt")
qlcv.read_from_File()
class MainCV:
    def them(maDuAn):
        qlcv.them(maDuAn= maDuAn)
    def sua(maDuAn):
        while(True):
            print('')
            qlcv.hienThi(maDuAn=maDuAn)
            print('=== Sửa thông tin ===')
            ma=input('Nhập mã công việc: CV_')
            if(ma!=''):
                ma = 'CV_'+ma
                break
        qlcv.timKiem(maDuAn,str(ma),'###')
        print('Nhập thông tin chỉnh sửa(Không sửa để trống)')
        ten = input('Tên công việc: ')
        moTa = input('Mô tả công việc: ')
        nguoiPhuTrach = input('Nhập tên người phụ trách : ')  # Đối tượng Employee
        ngayBatDau = input('Nhập ngày bắt đầu: ')  # Ngày bắt đầu thực tế
        ngayKetThuc = input('Nhập ngày kết thúc:')
        print('Trạng thái công việc(chọn 1-5)')
        print('1.Đang tiến hành')
        print('2.Quá hạn(Chậm tiến độ)')
        print('3.Đã huỷ')
        print('4.Tạm hoãn')
        print('5.Hoàn thành')
        tt = input('Trạng thái công việc: ')
        if (str(tt)=='1'):
            trangThai = 'Đang tiến hành'
        elif (str(tt)=='2'):
            trangThai = 'Quá hạn(Chậm tiến độ)'
        elif (str(tt)=='3'):
            trangThai = 'Đã huỷ'
        elif (str(tt)=='4'):
            trangThai = 'Tạm hoãn'
        elif (str(tt)=='5'):
            trangThai = 'Hoàn thành'
        trangThai=''
        for (i, cv) in enumerate(qlcv.Danh_Sach):
            if (cv.ma == ma):
                if(ten==''):
                    ten=cv.ten
                if(moTa==''):
                    moTa = cv.moTa
                if(nguoiPhuTrach==''):
                    nguoiPhuTrach = cv.nguoiPhuTrach
                if(trangThai==''):
                    trangThai = cv.trangThai
                if(ngayBatDau==''):
                    ngayBatDau = cv.ngayBatDau
                if(ngayKetThuc==''):
                    ngayKetThuc = cv.ngayKetThuc
        qlcv.suaThongTin(str(ma), str(ten), str(moTa), str(nguoiPhuTrach), str(trangThai), str(ngayBatDau), str(ngayKetThuc), str(maDuAn))
        qlcv.timKiem(maDuAn,str(ma),'###')
    def xoa(maDuAn):
        
        while(True):
            print('')
            qlcv.hienThi(maDuAn=maDuAn)
            print('=== Xoá công việc ===')
            ma=input('Nhập mã công việc: ')
            if(ma!=''):
                ma = 'CV_'+ma
                break
        qlcv.timKiem(maDuAn, ma,'###')
       
        while(True):
            print('Bạn có chắc chắn muốn xoá?')
            print('1.Yes')
            print('2.No')
            ip = input('Nhập lựa chọn: ')
            if (ip=='1'):
                qlcv.xoa(str(ma))
                break
            elif(ip=='2'):
                break
            else:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại!!!')
        from MQuanLyDuAn import call
        tn = call
        tn.CVmain(maDuAn=maDuAn)
    def timkiem(maDuAn):
        
        while(True):
            print('')
            qlcv.hienThi(maDuAn=maDuAn)
            print('=== Tìm kiếm công việc ===')
            cv=input('Nhập mã công việc hoặc tên công việc: ')
            if(cv!=''):
                break
        # cv=input('Nhập mã công việc hoặc tên công việc: ')
        qlcv.timKiem(maDuAn, str(cv), str(cv))
    def hienthi(maDuAn):
        qlcv.hienThi(maDuAn=maDuAn)


# qlcv.them('a')

# m = MainCV
# m.hienthi('a')
# m.sua('a')
# m.hienthi('a')
# m.xoa('a')
# m.hienthi('a')
# m.timkiem('a')




