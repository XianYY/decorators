__author__ = 'chenxian'


def debug(f):
    """
    the decorator to print function name, arguments names, argument values and return value
    :param f: a function
    :return: decorated function
    """

    def __combine_args(*args, **kws):
        arg_names = f.func_code.co_varnames
        arg_values = list(args)
        for name, default in zip(arg_names[len(args):], f.func_defaults):
            arg_values.append(kws[name] if name in kws else default)
        return ','.join(map(lambda t : '%s=%s'%(t[0], t[1]), zip(arg_names, arg_values)))

    def __f__(*args, **kws):
        ret = f(*args, **kws)
        print '%s with args %s then return %s'%(f.func_name, __combine_args(*args, **kws), str(ret))
        return ret
    return __f__