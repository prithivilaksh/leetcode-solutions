package lc
// type ZeroEvenOdd struct {
// 	n        int
//     zero     chan bool
//     odd      chan bool
//     even     chan bool
// }

// func NewZeroEvenOdd(n int) *ZeroEvenOdd {
// 	zeo := &ZeroEvenOdd{
// 		n:        n,
//         zero: make(chan bool,1),
//         odd: make(chan bool),
//         even: make(chan bool),
// 	}
//     zeo.zero<-true
// 	return zeo
// }

// func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
//     for i:=1;i<=z.n;i++{
//         <-z.zero
//         printNumber(0)
//         if i%2==0{
//             z.even<-true
//         }else{
//             z.odd<-true
//         }
//     }
//     close(z.even)
//     close(z.odd)
// }

// func (z *ZeroEvenOdd) Even(printNumber func(int)) {
//     for i:=2;i<=z.n;i+=2{
//         <-z.even
//         printNumber(i)
//         z.zero<-true
//     }
// }

// func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
//     for i:=1;i<=z.n;i+=2{
//         <-z.odd
//         printNumber(i)
//         z.zero<-true
//     }
// }


type ZeroEvenOdd struct {
	n        int
    zero     chan bool
    odd      chan int
    even     chan int
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	zeo := &ZeroEvenOdd{
		n:        n,
        zero: make(chan bool,1),
        odd: make(chan int),
        even: make(chan int),
	}
    zeo.zero<-true
	return zeo
}

func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
    for i:=1;i<=z.n;i++{
        <-z.zero
        printNumber(0)
        if i%2==0{
            z.even<-i
        }else{
            z.odd<-i
        }
    }
    close(z.even)
    close(z.odd)
}

func (z *ZeroEvenOdd) Even(printNumber func(int)) {
    for i:= range z.even {
        printNumber(i)
        z.zero<-true
    }
}

func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
    for i:= range z.odd {
        printNumber(i)
        z.zero<-true
    }
}