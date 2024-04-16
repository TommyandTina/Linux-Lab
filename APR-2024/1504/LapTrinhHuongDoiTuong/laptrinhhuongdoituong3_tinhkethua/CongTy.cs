using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong3_tinhkethua
{
    internal class TaoLapNhanVien
    {
        public static NhanVien TaoNhanVien(int loai)
        {
            if (loai == 1)
            {
                return new NhanVienSanXuat();
            }
            else
            {
                return new NhanVienVanPhong();
            }
        }

    }
    internal class CongTy
    {
        //thành phần dữ liệu
        private string _ten;
        private NhanVien[] _dsNhanVien;

        //thành phần xử lý
        public void Nhap(string ghiChu)
        {
            Console.WriteLine(ghiChu);
            Console.Write("Nhap ten cong ty: ");
            _ten = Console.ReadLine();
            Console.Write("Nhap so luong nhan vien : ");
            int n = int.Parse(Console.ReadLine());

            _dsNhanVien = new NhanVien[n];
            for (int i = 0; i < _dsNhanVien.Length; i++)
            {
                Console.Write("1. NNSX 2.NVVP");
                int loai = int.Parse(Console.ReadLine());
                _dsNhanVien[i] = TaoLapNhanVien.TaoNhanVien(loai);
                _dsNhanVien[i].Nhap($"Nhap thong tin nhan vien thu {i+1}: ");
            }


        }
        
        public double TinhTongLuong()
        {
            double s = 0;
            for (int i =0; i < _dsNhanVien.Length; i++)
            {
                s = s + _dsNhanVien[i].TinhLuong();
            }
            return s;
        }

    }
}
