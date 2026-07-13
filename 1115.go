package lc

// type FooBar struct {
// 	n int
//     mu *sync.RWMutex
//     foo bool
// }

// func NewFooBar(n int) *FooBar {
// 	return &FooBar{n: n, mu:&sync.RWMutex{}, foo:true}
// }

// func (fb *FooBar) Foo(printFoo func()) {
// 	for i := 0; i < fb.n; i++ {
// 		// printFoo() outputs "foo". Do not change or remove this line.
//         fb.mu.Lock()
//         if fb.foo==true{
//             printFoo()
//             fb.foo=false
//         }else{
//             i--
//         }
//         fb.mu.Unlock()
// 	}
// }

// func (fb *FooBar) Bar(printBar func()) {
// 	for i := 0; i < fb.n; i++ {
// 		// printBar() outputs "bar". Do not change or remove this line.
//         fb.mu.Lock()
//         if fb.foo==false{
//             printBar()
//             fb.foo=true
//         }else{
//             i--
//         }
//         fb.mu.Unlock()
// 	}
// }

type signal = struct{}
type FooBar struct {
	n int
    foo chan signal
    bar chan signal
}

func NewFooBar(n int) *FooBar {
    foo,bar:=make(chan signal,1), make(chan signal)
    foo<-signal{}
	return &FooBar{n: n,foo:foo,bar:bar}
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
		// printFoo() outputs "foo". Do not change or remove this line.
        <-fb.foo
        printFoo()
        fb.bar<-signal{}
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
		// printBar() outputs "bar". Do not change or remove this line.
        <-fb.bar
        printBar()
        fb.foo<-signal{}
	}
}