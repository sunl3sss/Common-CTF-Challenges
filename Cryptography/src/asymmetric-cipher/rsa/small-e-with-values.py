#!/usr/bin/env python

# Change values
e = 3
n1 = 95118357989037539883272168746004652872958890562445814301889866663072352421703264985997800660075311645555799745426868343365321502734736006248007902409628540578635925559742217480797487130202747020211452620743021097565113059392504472785227154824117231077844444672393221838192941390309312484066647007469668558141
n2 = 98364165919251246243846667323542318022804234833677924161175733253689581393607346667895298253718184273532268982060905629399628154981918712070241451494491161470827737146176316011843738943427121602324208773653180782732999422869439588198318422451697920640563880777385577064913983202033744281727004289781821019463
n3 = 68827940939353189613090392226898155021742772897822438483545021944215812146809318686510375724064888705296373853398955093076663323001380047857809774866390083434272781362447147441422207967577323769812896038816586757242130224524828935043187315579523412439309138816335569845470021720847405857361000537204746060031
c1 = 64830446708169012766414587327568812421130434817526089146190136796461298592071238930384707543318390292451118980302805512151790248989622269362958718228298427212630272525186478627299999847489018400624400671876697708952447638990802345587381905407236935494271436960764899006430941507608152322588169896193268212007
c2 = 96907490717344346588432491603722312694208660334282964234487687654593984714144825656198180777872327279250667961465169799267405734431675111035362089729249995027326863099262522421206459400405230377631141132882997336829218810171728925087535674907455584557956801831447125486753515868079342148815961792481779375529
c3 = 43683874913011746530056103145445250281307732634045437486524605104639785469050499171640521477036470750903341523336599602288176611160637522568868391237689241446392699321910723235061180826945464649780373301028139049288881578234840739545000338202917678008269794179100732341269448362920924719338148857398181962112


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def find_invpow(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high / 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x: low = mid
        elif high > mid and mid**n > x: high = mid
        else: return mid
    return mid + 1

flag_cubed = chinese_remainder([n1, n2, n3],[c1, c2, c3])
flag = find_invpow(flag_cubed, 3)

print "flag: ",hex(flag)[2:-1].decode("hex")