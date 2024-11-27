from entity import Entity

class DuAn(Entity):
    def __init__(self, ma ='', ten ='',loaiDuAn ='', moTa ='', ngayBatDau ='', ngayKetThuc ='', nganSach ='', trangThai =''):
        super().__init__(ma, ten)
        self.ma = ma
        self.ten = ten
        self.loaiDuAn = loaiDuAn
        self.moTa = moTa
        self.ngayBatDau = ngayBatDau
        self.ngayKetThuc = ngayKetThuc
        self.nganSach = nganSach
        self.trangThai = trangThai  # Ví dụ: 'Đang tiến hành', 'Hoàn thành', 'Đã hủy'
        # self.lstCongViec = []  # Danh sách các công việc thuộc dự 
        # self.lstNhanVien = []
    def NhapThongTin(self):
        print('=== Nhập thông tin dự án ===')
        ma= qlda.maTuSinh()
        self.ma = ma
        # self.ma = input('Mã dự án: ')
        self.ten = input('Tên dự án: ') 
        self.loaiDuAn = input('Loại dự án: ')
        self.moTa = input('Mô tả dự án: ')
        self.ngayBatDau = input('Ngày bắt đầu dự án: ')
        self.ngayKetThuc = input('Ngày kết thúc dự án: ')
        self.nganSach = input('Ngân sách dự án: ')
        while(True):
            print('Trạng thái dự án(chọn 1-5)')
            print('1.Đang tiến hành')
            print('2.Quá hạn(Chậm tiến độ)')
            print('3.Đã huỷ')
            print('4.Tạm hoãn')
            print('5.Hoàn thành')
            tt = input('Trạng thái dự án: ')
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
        if (self.ma!=''
            and self.ten!=''
            and self.loaiDuAn!=''
            and self.moTa!=''
            and self.ngayBatDau!=''
            and self.ngayKetThuc!=''
            and self.nganSach!=''
            and self.trangThai!=''
              ):
            print('Nhập Thông tin dự án thành công')
            print('')
            print('Thông tin dự án mới:')
            print(f'Mã dự án: {self.ma}')
            print(f'Tên dự án: {self.ten}') 
            print(f'Loại dự án: {self.loaiDuAn}')
            print(f'Mô tả dự án: {self.moTa}')
            print(f'Ngày bắt đầu dự án: {self.ngayBatDau}')
            print(f'Ngày kết thúc dự án: {self.ngayKetThuc}')
            print(f'Ngân sách dự án: {self.nganSach}')
            print(f'Trạng thái dự án: {self.trangThai}')
        else:
            while(True):
                print('')
                print('Vui lòng nhập đầy đủ thông tin')
                check=True
                if (self.ma==''):
                    check=False
                    self.ma = input('Mã dự án: ')
                else:
                    print(f'Mã dự án: {self.ma}')
                if (self.ten==''):
                    check=False
                    self.ten = input('Tên dự án: ')
                else:
                    print(f'Tên dự án: {self.ten}')      
                if (self.loaiDuAn==''):
                    check=False
                    self.loaiDuAn = input('Loại dự án: ')
                else:
                    print(f'Loại dự án: {self.loaiDuAn}')
                if (self.moTa==''):
                    check=False
                    self.moTa = input('Mô tả dự án: ')
                else:
                    print(f'Mô tả dự án: {self.moTa}')
                if (self.ngayBatDau==''):
                    check=False
                    self.ngayBatDau = input('Ngày bắt đầu dự án: ')
                else:
                    print(f'Ngày bắt đầu dự án: {self.ngayBatDau}')
                if (self.ngayKetThuc==''):
                    check=False
                    self.ngayKetThuc = input('Ngày kết thúc dự án: ')
                else:
                    print(f'Ngày kết thúc dự án: {self.ngayKetThuc}')
                if (self.nganSach==''):
                    check=False
                    self.nganSach = input('Ngân sách dự án: ')
                elif(self.nganSach.isdigit()==False):
                    self.nganSach=0
                else:
                    print(f'Ngân sách dự án: {self.nganSach}')
                if (self.trangThai=='' and self.trangThai!='1' and self.trangThai!='2' and self.trangThai!='3' and self.trangThai!='4' and self.trangThai!='5'):
                    check=False
                    print('Trạng thái dự án(chọn 1-5)')
                    print('1.Đang tiến hành')
                    print('2.Quá hạn(Chậm tiến độ)')
                    print('3.Đã huỷ')
                    print('4.Tạm hoãn')
                    print('5.Hoàn thành')
                    tt = input('Trạng thái dự án: ')
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
                else:
                    print(f'Trạng thái dự án: {self.trangThai}')
                if (self.ma!=''
                and self.ten!=''
                and self.loaiDuAn!=''
                and self.moTa!=''
                and self.ngayBatDau!=''
                and self.ngayKetThuc!=''
                and self.nganSach!=''
                and self.trangThai!=''
                ):
                    print('Nhập Thông tin dự án thành công')
                    print('')
                    print('Thông tin dự án mới:')
                    print(f'Mã dự án: {self.ma}')
                    print(f'Tên dự án: {self.ten}') 
                    print(f'Loại dự án: {self.loaiDuAn}')
                    print(f'Mô tả dự án: {self.moTa}')
                    print(f'Ngày bắt đầu dự án: {self.ngayBatDau}')
                    print(f'Ngày kết thúc dự án: {self.ngayKetThuc}')
                    print(f'Ngân sách dự án: {self.nganSach}')
                    print(f'Trạng thái dự án: {self.trangThai}')
                    break
        while(True):
            print('')
            print('00.Quay lại')
            op=input('Nhập lựa chọn của bạn: ')
            if (op=="00"):
                break
            else:
                print('Lựa chọn không hợp lệ')
    def toString(self): return '#*'.join([str(self.ma), str(self.ten), str(self.loaiDuAn), str(self.moTa), str(self.ngayBatDau), (self.ngayKetThuc), str(self.nganSach), str(self.trangThai)])
class QLDuAn:
    def __init__(self, file_path):
            self.Danh_Sach = list() #Tạo danh sách trống
            self.file_path =file_path
    def read_from_File(self):
       file = open(self.file_path,'r', encoding='utf-8')
       Lines = file.readlines() #lấy từng dòng của file rồi cho vào danh sách Lines
       file.close()
       self.Danh_Sach = list()
       for da in Lines:#duyệt từng phần tử của Lines
           tmp=da.split('#*')#tách các phần tử đc ngăn cách bằng #* rồi cho vào lst tmp, lúc lưu ngăn cách bằng #*
           if (len(tmp)==8):
                dn = DuAn(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6],tmp[7])#tạo đối tượng Monhoc mới maMH, tenMH, soTC
                self.Danh_Sach.append(dn)#thêm DuAn vào cuối danh sách    
    def write2File(self):
            file = open(self.file_path, 'w', encoding='utf-8')#mở file để ghi dữ liệu, dữ liệu cũ sẽ bị xoá
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
            if( ma != da.ma for da in self.Danh_Sach):
                break
        return ma
    def them(self):
            print('')
            qlda.hienThi()
            print('=== Thêm dự án mới===')
            da = DuAn()
            da.NhapThongTin()
            self.Danh_Sach.append(da)
            file = open(self.file_path, 'a', encoding='utf-8')
            file.write('\n'+da.toString()) #ghi vào cuối file
            file.close()
            self.hienThi()
            print('Thêm dự án thành công.')   
    def suaThongTin(self, ma=None, ten=None, loaiDuAn=None, moTa=None, ngayBatDau=None, ngayKetThuc=None, nganSach=None, trangThai=None):
        check = False
        for (i, da) in enumerate(self.Danh_Sach):
            if (da.ma == ma):
                da.ten = ten
                da.loaiDuAn = loaiDuAn
                da.moTa = moTa
                da.ngayBatDau = ngayBatDau
                da.ngayKetThuc = ngayKetThuc
                da.nganSach = nganSach
                da.trangThai = trangThai
                self.write2File()
                check = True
        if(check==True):
            print('Sửa thông tin thành công.')
        else:
            print('Sửa thông tin không thành công.')
    def xoa(self, ma):
        xoa = 0
        for (i, da) in enumerate(self.Danh_Sach):
            if (da.ma == ma):
                self.Danh_Sach.remove(da)
                xoa = 1
                # Nếu có hành động xoá môn học thì update file
        if (xoa == 1):
              print('=== Xoá dự án thành công ===') 
              self.write2File()
        else:
              print('=== Xoá dự án không thành công ===')
    def TimKiem(self, ma='', ten=''):
        print('')
        print('=== Danh sách dự án ===')
        # Find maximum string lengths for each column
        maxstrma = max(len(da.ma) for da in self.Danh_Sach)
        if(maxstrma<len('Mã dự án')):
            maxstrma=len('Mã dự án')
        maxstrten = max(len(da.ten) for da in self.Danh_Sach)
        if(maxstrten<len('Tên dự án')):
            maxstrten=len('Tên dự án')
        maxstrloaiDuAn = max(len(da.loaiDuAn) for da in self.Danh_Sach)
        if(maxstrloaiDuAn<len('Loại dự án')):
            maxstrloaiDuAn=len('Loại dự án')
        maxstrmoTa = max(len(da.moTa) for da in self.Danh_Sach)
        if(maxstrmoTa<len('Mô tả dự án')):
            maxstrmoTa=len('Mô tả dự án')
        maxstrngayBatDau = max(len(da.ngayBatDau) for da in self.Danh_Sach)
        if(maxstrngayBatDau<len('Ngày bắt đầu')):
            maxstrngayBatDau=len('Ngày bắt đầu')
        maxstrngayKetThuc = max(len(da.ngayKetThuc) for da in self.Danh_Sach)
        if(maxstrngayKetThuc<len('Ngày kết thúc')):
            maxstrngayKetThuc=len('Ngày kết thúc')
        maxstrnganSach = max(len(str(da.nganSach)) for da in self.Danh_Sach)
        if(maxstrnganSach<len('Ngân sách')):
            maxstrnganSach=len('Ngân sách')
        maxstrtrangThai = max(len(da.trangThai) for da in self.Danh_Sach)
        if(maxstrtrangThai<len('Trạng thái')):
            maxstrtrangThai=len('Trạng thái')
        # Print the header row
        headerformat = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrloaiDuAn}}}\t{{:<{maxstrmoTa}}}\t{{:<{maxstrngayBatDau}}}\t{{:<{maxstrngayKetThuc}}}\t{{:<{maxstrnganSach}}}\t{{:<{maxstrtrangThai}}}"
        print(headerformat.format("STT", "Mã dự án", "Tên dự án", "Loại dự án","Mô tả","Ngày bắt đầu","Ngày kết thúc","Ngân sách","Trạng thái"))
       
        # print('STT\tMã dự án\tTên dự án\tLoại dự án\tMô tả\tNgày Bắt đầu\tNgày kết thúc\tNgân sách\tTrạng thái')
        sl = 0
        for (i, da) in enumerate(self.Danh_Sach):
            if (da.ma.lower().__contains__(ma.lower())# contains = in
                    or da.ten.lower().__contains__(ten.lower())):
                sl = sl + 1
                # print('\t'.join([str(sl), mh.maMH, mh.tenMH, str(mh.soTC)]))
                row_format = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrloaiDuAn}}}\t{{:<{maxstrmoTa}}}\t{{:<{maxstrngayBatDau}}}\t{{:<{maxstrngayKetThuc}}}\t{{:<{maxstrnganSach}}}\t{{:<{maxstrtrangThai}}}"
                print(row_format.format(str(sl), da.ma, da.ten, da.loaiDuAn, da.moTa,da.ngayBatDau,da.ngayKetThuc,da.nganSach,da.trangThai))
        if (sl == 0):
            print("Không có dự án nào thoả mãn yêu cầu tìm kiếm")
    def hienThi(self):
        print('')
        print('=== Danh sách dự án ===')
        # Find maximum string lengths for each column
        maxstrma = max(len(da.ma) for da in self.Danh_Sach)
        if(maxstrma<len('Mã dự án')):
            maxstrma=len('Mã dự án')
        maxstrten = max(len(da.ten) for da in self.Danh_Sach)
        if(maxstrten<len('Tên dự án')):
            maxstrten=len('Tên dự án')
        maxstrloaiDuAn = max(len(da.loaiDuAn) for da in self.Danh_Sach)
        if(maxstrloaiDuAn<len('Loại dự án')):
            maxstrloaiDuAn=len('Loại dự án')
        maxstrmoTa = max(len(da.moTa) for da in self.Danh_Sach)
        if(maxstrmoTa<len('Mô tả dự án')):
            maxstrmoTa=len('Mô tả dự án')
        maxstrngayBatDau = max(len(da.ngayBatDau) for da in self.Danh_Sach)
        if(maxstrngayBatDau<len('Ngày bắt đầu')):
            maxstrngayBatDau=len('Ngày bắt đầu')
        maxstrngayKetThuc = max(len(da.ngayKetThuc) for da in self.Danh_Sach)
        if(maxstrngayKetThuc<len('Ngày kết thúc')):
            maxstrngayKetThuc=len('Ngày kết thúc')
        maxstrnganSach = max(len(str(da.nganSach)) for da in self.Danh_Sach)
        if(maxstrnganSach<len('Ngân sách')):
            maxstrnganSach=len('Ngân sách')
        maxstrtrangThai = max(len(da.trangThai) for da in self.Danh_Sach)
        if(maxstrtrangThai<len('Trạng thái')):
            maxstrtrangThai=len('Trạng thái')
        # Print the header row
        headerformat = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrloaiDuAn}}}\t{{:<{maxstrmoTa}}}\t{{:<{maxstrngayBatDau}}}\t{{:<{maxstrngayKetThuc}}}\t{{:<{maxstrnganSach}}}\t{{:<{maxstrtrangThai}}}"
        print(headerformat.format("STT", "Mã dự án", "Tên dự án", "Loại dự án","Mô tả","Ngày bắt đầu","Ngày kết thúc","Ngân sách","Trạng thái"))
        # Print the body rows
        for i, da in enumerate(self.Danh_Sach):
            row_format = f"{{:<3}}\t{{:<{maxstrma}}}\t{{:<{maxstrten}}}\t{{:<{maxstrloaiDuAn}}}\t{{:<{maxstrmoTa}}}\t{{:<{maxstrngayBatDau}}}\t{{:<{maxstrngayKetThuc}}}\t{{:<{maxstrnganSach}}}\t{{:<{maxstrtrangThai}}}"
            print(row_format.format(i+1, da.ma, da.ten, da.loaiDuAn, da.moTa,da.ngayBatDau,da.ngayKetThuc,da.nganSach,da.trangThai))

qlda = QLDuAn('QuanLyDuAn.txt')
qlda.read_from_File()
class MainDA:
    
    def them():
        qlda.them()
    def sua():
        while(True):
            print('')
            qlda.hienThi()
            print('=== Sửa thông tin dự án ===')
            ma = input('Nhập mã dự án: DA_')
            if(ma!=''):
                ma='DA_'+ma
                break
        qlda.TimKiem(str(ma),'###')
        print('Thông tin chỉnh sửa(Không sửa để trống)')
        ten = input('Tên dự án: ') 
        loaiDuAn = input('Loại dự án: ')
        moTa = input('Mô tả dự án: ')
        ngayBatDau = input('Ngày bắt đầu dự án: ')
        ngayKetThuc = input('Ngày kết thúc dự án: ')
        nganSach = input('Ngân sách dự án: ')
        trangThai=''
        print('Trạng thái dự án(chọn 1-5)')
        print('1.Đang tiến hành')
        print('2.Quá hạn(Chậm tiến độ)')
        print('3.Đã huỷ')
        print('4.Tạm hoãn')
        print('5.Hoàn thành')
        tt = input('Trạng thái dự án: ')
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
        for (i, da) in enumerate(qlda.Danh_Sach):
            if (da.ma.strip().lower()==(ma.strip().lower())):
                if(ten==''):
                    ten= da.ten
                if(loaiDuAn==''):
                    loaiDuAn= da.loaiDuAn
                if(moTa==''):
                    moTa= da.moTa
                if(ngayBatDau==''):
                    ngayBatDau= da.ngayBatDau
                if(ngayKetThuc==''):
                    ngayKetThuc= da.ngayKetThuc
                if(nganSach==''):
                    nganSach= da.nganSach
                if(trangThai==''):
                    trangThai= da.trangThai
        qlda.suaThongTin(str(ma), ten, loaiDuAn, moTa, ngayBatDau, ngayKetThuc, nganSach, trangThai)
        while(True):
            qlda.TimKiem(str(ma),'###')
            print('')
            print('00.Quay lại')
            op=input('Nhập lựa chọn của bạn: ')
            if (op=='00'):
                from MQuanLyDuAn import call
                tn = call
                tn.setnull()
            else:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại')
    def xoa():
        # qlda.hienThi()
        # print('')
        # print('=== Xoá dự án ===')
        # ma = input('Nhập mã dự án: ')
        while(True):
            print('')
            qlda.hienThi()
            print('=== Xoá dự án ===')
            ma = input('Nhập mã dự án: DA_')
            if(ma!=''):
                ma='DA_'+ma
                break
        qlda.TimKiem(str(ma),"###")
        while(True):
            print('Bạn có chắc chắn muốn xoá?')
            print('1.Yes')
            print('2.No')
            ip = input('Nhập lựa chọn: ')
            if (ip=='1'):
                qlda.xoa(str(ma))
                from MQuanLyDuAn import call
                tn = call
                tn.setnull()
            elif(ip=='2'):
                # fix
                from MQuanLyDuAn import call
                tn = call
                tn.setnull()
            else:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại!!!')
    def timkiem():
        print('')
        print('=== Tìm kiếm dự án ===')
        tt=input('Nhập mã dự án hoặc tên dự án: ')
        while(True):
            qlda.TimKiem(str(tt), str(tt))
            print('')
            print('00.Quay lại')
            op=input('Nhập lựa chọn của bạn: ')
            if (op=='00'):
                from MQuanLyDuAn import call
                tn = call
                tn.setnull()
            else:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại')
    def hienthi():
        qlda.hienThi()
# qlda = QLDuAn('QuanLyDuAn.txt')
# qlda.read_from_File()
# qlda.them
# qlda.hienThi()
# qlda.TimKiem('2','2')
# m= MainDA
# m.hienthi()













