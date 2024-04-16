using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong3_tinhkethua
{
    internal class NhanVien
    {
        public string HoTen { get; set; }
        public string DiaChi { get; set; }
        public string CCCD { get; set; }

        public NhanVien()
        {
            Console.WriteLine("HAM TAO NHAN VIEN 1: KO DOI SO");
        }
        public NhanVien(string t)
        {
            this.HoTen = t;
            Console.WriteLine("HAM TAO NHAN VIEN 2: CO DOI SO");
        }

        public virtual void Nhap(string ghiChu)
        {
            Console.WriteLine(ghiChu);
            Console.Write("Nhap ho ten: ");
            HoTen = Console.ReadLine();
            Console.Write("Nhap dia chi: ");
            DiaChi = Console.ReadLine();
            Console.Write("Nhap cccd: ");
            CCCD = Console.ReadLine();
        }

        public virtual double TinhLuong()
        {
            return 0;
        }
    }
}
