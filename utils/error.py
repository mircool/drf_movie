def response_data(status_code=0, message=None, data=None, **kwargs):
    if message is None:
        message = 'success'

    return dict({
        'status_code': status_code,
        'message': message,
        'data': data
    }, **kwargs)


class MovieError:
    MovieNotFound = (1000, '电影信息不存在')
    MovieAlreadyExist = (1001, '电影信息已存在')
    MovieCreateError = (1002, '电影信息创建失败')
    MovieUpdateError = (1003, '电影信息更新失败')
    MovieDeleteError = (1004, '电影信息删除失败')
    MovieListError = (1005, '电影信息列表获取失败')
    MovieListEmpty = (1006, '电影信息列表为空')


class UserError:
    UserNotFound = (2000, '用户信息不存在')
    UserAlreadyExist = (2001, '用户信息已存在')
    UserCreateError = (2002, '用户信息创建失败')
    UserUpdateError = (2003, '用户信息更新失败')
    UserDeleteError = (2004, '用户信息删除失败')
    UserListError = (2005, '用户信息列表获取失败')
    UserListEmpty = (2006, '用户信息列表为空')


class Trade:
    CardParamError = (3000, '参数错误')
    OrderCreateError = (3001, '订单创建失败')
    PayrequestError = (3002, '支付请求失败')
    ProfileError = (3003, '用户信息不存在')
    UnexpectedError = (3004, '未知错误')
