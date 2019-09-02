from time import ctime, sleep, time
import threading


def music(musicName):
    for i in range(3):
        print("I was listening %s, %s" % (musicName, ctime()))
        sleep(1)


def move(moveName):
    for i in range(2):
        print("I was at the %s! %s" % (moveName, ctime()))
        sleep(3)


exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        printTime(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def printTime(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        sleep(delay)
        print("%s: %s" % (threadName, ctime(time())))
        counter -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=music, args=(u'爱我1中华',))
    t2 = threading.Thread(target=move, args=(u'战狼',))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # # 创建新线程
    # thread1 = MyThread(1, "Thread-1", 1)
    # thread2 = MyThread(2, "Thread-2", 2)
    #
    # # 开启新线程
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    # thread1.start()
    # thread2.start()

    print('主进程退出 %s' % ctime(time()))

# gp      git push

# gup     git pull --rebase
# gupv    git pull --rebase -v

# gco     git checkout
# gcm     git checkout master
# gcd     git checkout develop
# gcb     git checkout -b

# grh     git reset HEAD
# grhh    git reset HEAD --hard

# grb     git rebase
# grbi    git rebase -i
# grbm    git rebase master
# grba    git rebase --abort
# grbc    git rebase --continue

# gst     git status
# gss     git status -s
# gsb     git status -sb

# gsta    git stash save
# gstaa   git stash apply
# gstc    git stash clear
# gstl    git stash list
# gstp    git stash pop
# gsts    git stash show --text

# ga      git add
# gaa     git add all

# gb      git branch
# gba     git branch -a
# gbd     git branch -d

# gr      git remote
# gra     git remote add
# grv     git remote -v
# grup    git remote update
# grmv    git remote rename
# grrm    git remote remove
# grset   git remote set-url

# gc      git commit -v
# gc!     git commit -v --amend
# gcn!    git commit -v --no-edit --amend
# gca     git commit -v -a
# gca!    git commit -v -a --amend
# gcan!   git commit -v -a --no-edit --amend
# gcans!  git commit -v -a -s --no-edit --amend
# gcam    git commit -a -m
# gcsm    git commit -s -m
# gcmsg   git commit -m
# gcs     git commit -S



