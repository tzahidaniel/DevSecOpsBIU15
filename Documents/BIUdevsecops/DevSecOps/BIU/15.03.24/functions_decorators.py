def add_defaults(two_params_func):
    def two_params_with_defaults_func(a=0, b=0):
        return two_params_func(a,b)
    return two_params_with_defaults_func

def sub_nums(a, b):
    print(a - b)

sub_nums(9)

better_sub = add_defaults(sub_nums)

better_sub(9, 6)

better_sub(9)

sub_nums = add_defaults(sub_nums)

sub_nums(9 - 4)
sub_nums(9 , 4)


#################

def add_defaults(two_params_func):
    def two_params_with_defaults_func(a=0, b=0):
        return two_params_func(a,b)
    return two_params_with_defaults_func


@add_defaults
def mult_nums(x, y):
    print(x * y)


def div_nums(x, y):
    print(x / y)

mult_nums(2, 3)

mult_nums(2)

div_nums(10, 2)

div_nums(10)

##################






def add_hi(original_func):
    def new_func(a , b):
        print('hi')
        original_func(a, b)
    return new_func

def get_2nd(a, b):
    print(b)

get_2nd(15, "good")

get_2nd = add_hi(get_2nd)
