using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong2
{
    internal class Diem
    {
        public int X{ get; set; }
        public int Y{ get; set; }

        public Diem()
        {
            X = 0;
            Y = 0;
        }
        public Diem(int x, int y)
        {
            X= x;
            Y= y;
        }
        public void Nhap (string ghiChu)
        {
            Console.WriteLine(ghiChu);
            Console.WriteLine("Nhap toa do X:");
            X = int.Parse(Console.ReadLine());
            Console.WriteLine("Nhap toa do Y:");
            Y = int.Parse(Console.ReadLine());

        }    
        public double TinhKhoangCach(Diem b)
        {
            return Math.Sqrt((X - b.X) * (X - b.X) + (Y- b.Y) * (Y - b.Y));
        }
    }
}
