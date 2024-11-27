from quanlyduan import DuAn, QLDuAn, MainDA
from NhanVien import NhanVien, QLNhanVien, MainNV
from TaiNguyen import TaiNguyen, QLTaiNguyen, mainTN
from Congviec import CongViec, QLCongViec, MainCV
# DỰ ÁN
da = MainDA
qlda = QLDuAn('QuanLyDuAn.txt')
qlda.read_from_File()
# TÀI NGUYÊN
tn = mainTN
# NHÂN VIÊN
nv = MainNV
# CÔNG VIỆC
cv = MainCV
class DAmain():
    def setnull(self):
        da.hienthi()
        self.duancs()
    def duancs(self):
        while ( True):
            print('')
            print('=== QUẢN LÝ DỰ ÁN ===')
            print('1.Thêm dự án')
            print('2.Sửa dự án')
            print('3.Xoá dự án')
            print('4.Tìm kiếm dự án')
            print('5.Xem chi tiết thông tin dự án')
            op=input('NHẬP LỰA CHỌN TƯƠNG ỨNG: ')
            if (op=='1'):
                da.them()
            elif (op=='2'):
                da.sua()
            elif(op=='3'):
                da.xoa()
            elif(op=='4'):
                da.timkiem()
            elif(op=='5'):
                self.xemchitiet()
            else:
                da.hienthi()
                print('Lựa chọn không hợp lệ!!!')
                self.duancs()
    def xemchitiet(self):
        da.hienthi()
        while (True):
            print('')
            print('=== Xem chi tiết dự án ===')
            ma = input('Nhập mã sự án: ')
            qlda.TimKiem(str(ma),'###')
            while (True):
                print('1.Xem công việc')
                print('2.Xem nhân viên')
                print('3.Xem tài nguyên')
                print('00.Quay lại')
                op =input('Nhập lựa chọn tương ứng: ')
                if (op == '1'):
                    self.CVmain(maDuAn=ma)
                elif(op == '2'):
                    self.NVmain(maDuAn=ma)
                elif(op == '3'):
                    self.TNmain(maDuAn= ma)
                elif(op == '00'):
                    self.setnull()
                else:
                    da.hienthi()
                    print('Lựa chọn không hợp lệ!!!')
                    self.xemchitiet()
    def TNmain(self, maDuAn):
        tn.hienthi(ma = maDuAn)
        self.tncs(maDuAn= maDuAn)
    def tncs(self, maDuAn):
        while (True):
            print('')
            print('=== QUẢN LÝ TÀI NGUYÊN ===')
            print('1.Thêm tài nguyên')
            print('2.Sửa tài nguyên')
            print('3.Xoá tài nguyên')
            print('4.Tìm kiếm tài nguyên')
            print('5.Xem tài nguyên')
            print('00.Quay lại')
            op=input('NHẬP LỰA CHỌN TƯƠNG ỨNG: ')
            if (op=='1'):
                tn.them(maDuAn=maDuAn)
            elif (op=='2'):
                tn.sua()
            elif(op=='3'):
                tn.xoa(maDuAn= maDuAn)
            elif(op=='4'):
                tn.timkiem(maDuAn=maDuAn)
                self.tncs(maDuAn=maDuAn)
            elif(op=='5'):
                tn.hienthi(ma = maDuAn)
            elif(op=='00'):
                mn.setnull()
            else:
                tn.hienthi(ma = maDuAn)
                print('Lựa chọn không hợp lệ!!!')
                self.tncs(maDuAn= maDuAn)
    def NVmain(self, maDuAn):
        nv.hienthi(ma= maDuAn)
        self.nvcs(maDuAn= maDuAn)
    def nvcs(self,maDuAn):
         while ( True):
            print('')
            print('=== QUẢN LÝ NHÂN VIÊN ===')
            print('1.Thêm nhân viên')
            print('2.Sửa nhân viên')
            print('3.Xoá nhân viên')
            print('4.Tìm kiếm nhân viên')
            print('5.Xem nhân viên')
            print('00.Quay lại')
            op=input('NHẬP LỰA CHỌN TƯƠNG ỨNG:')
            if (op=='1'):
                nv.them(ma=maDuAn)
            elif (op=='2'):
                nv.sua(maDuAn= maDuAn)
            elif(op=='3'):
                nv.xoa(maDuAn=maDuAn)
            elif(op=='4'):
                nv.timkiem(maDuAn=maDuAn)
            elif(op=='5'):
                nv.hienthi(ma = maDuAn)
            elif(op=='00'):
                mn.setnull()
            else:
                nv.hienthi(ma= maDuAn)
                print('Lựa chọn không hợp lệ!!!')
                self.nvcs(maDuAn= maDuAn)            
    def CVmain(self, maDuAn):
            cv.hienthi(maDuAn= maDuAn)
            self.cvcs(maDuAn= maDuAn)
    def cvcs(self,maDuAn):
         while ( True):
            print('')
            print('=== QUẢN LÝ CÔNG VIỆC ===')
            print('1.Thêm công việc')
            print('2.Sửa công việc')
            print('3.Xoá công việc')
            print('4.Tìm kiếm công việc')
            print('5.Xem công việc')
            print('00.Quay lại')
            op=input('NHẬP LỰA CHỌN TƯƠNG ỨNG:')
            if (op=='1'):
                cv.them(maDuAn=maDuAn)
            elif (op=='2'):
                cv.sua(maDuAn= maDuAn)
            elif(op=='3'):
                cv.xoa(maDuAn=maDuAn)
            elif(op=='4'):
                cv.timkiem(maDuAn=maDuAn)
            elif(op=='5'):
                cv.hienthi(maDuAn = maDuAn)
            elif(op=='00'):
                mn.setnull()
            else:
                cv.hienthi(maDuAn= maDuAn)
                print('Lựa chọn không hợp lệ!!!')
                self.cvcs(maDuAn= maDuAn)
                print('Lựa chọn không hợp lệ!!!')

# thêm chức năng thống kê
mn=DAmain()
# mn.setnull()

class call():
    def setnull():
        mn.setnull()
    def TNmain(maDuAn):
        mn.TNmain(maDuAn= maDuAn)
    def NVmain(maDuAn):
        mn.NVmain(maDuAn=maDuAn)
    def CVmain(maDuAn):
        mn.CVmain(maDuAn=maDuAn)
    def duancs():
        mn.duancs()
m = call
m.setnull()



