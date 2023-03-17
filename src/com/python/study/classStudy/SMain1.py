from src.com.python.study.classStudy.SingltonRepository import SingltonRepository

if __name__ == '__main__':
    userRepository = SingltonRepository.getInstance()
    userRepository.userList.append("user1")
    print(userRepository.userList)
    from src.com.python.study.classStudy.SMain2 import test
    test()