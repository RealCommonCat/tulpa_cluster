import pandas as pd
# 读取Excel文件
result = []
# 1.身体的年龄是？	
# 2.身体的性别是？	
# 3.在目前的T家四分类法中你们属于哪一类呢？(一类)
# 4.(二类)	
# 5.(三类)	
# 6.(四类)	
# 7.(不知道t家四分类是什么)	
# 8.在埃蒙加德环中，你们认为自己属于哪一类呢？	
# 9.在创造第一个tulpa之前，你（们）曾经是？	
# 10.你们系统目前拥有多少名成员呢？（包括宿主）	
# 11.你们系统中目前有多少名tulpa呢	
# 12.在创造第一个tulpa时，身体多少岁呢？	
# 13.在创造第一个tulpa时，从开始到成声或者产生可思考的意识花了多久呢（单位:月）（可以问问tulpa本人哦）	
# 14.你们加入tulpa社区多久了呢？（单位：月）	
# 15.你们系统中最成熟的tulpa活跃度如何呢？	
# 16.你们系统中有系魂吗？如果有，那么包括以下哪一种情况呢？(已经放弃系魂认同的前系魂)	
# 17.(原创角色系魂)	
# 18.(非原创但是脱离原角色的系魂)	
# 19.(非原创且没有脱离原角色的系魂)	
# 20.(其他)	
# 21.(没有系魂)	
# 22.你们目前有加入隔壁多意识体社区吗？	
# 23.请问你们的身体有哪些精神疾病/症状呢？—轻度抑郁	
# 24.中度及以上抑郁	
# 25.轻度焦虑	
# 26.中度及以上焦虑	
# 27.双相情感障碍	
# 28.精神分裂症	
# 29.强迫症	
# 30.孤独症谱系障碍	
# 31.注意缺陷多动障碍	
# 32.创伤后应激障碍（PTSD）	
# 33.复杂型创伤后应激障碍 (C-PTSD)	
# 34.分离性身份障碍（DID）	
# 35.其他特定分离性障碍（OSDD）（或p-did）	
# 36.人格解体/现实解体	
# 37.神经衰弱	
# 38.请问你们还有上面未提到的精神疾病吗？	
# 39.请问你们是从哪里得知tulpa的呢？	
# 40.一开始为什么要创造tulpa呢？(需要爱和陪伴)	
# 41.(希望有能完全理解自己的人)	
# 42.(希望tulpa能够帮助对抗精神疾病)	
# 43.(因为喜欢某个角色所以创造了以ta为原型的tulpa)	
# 44.(意外创造（当时没有料到tulpa可以有意识）)	
# 45.(儿时的幻想朋友)	
# 46.(因为朋友/认识的人有)	
# 47.(其他)	
# 48.在创造tulpa期间，宿主的精神状态总体上如何呢？	
# 49.创造tulpa的过程发生在哪里呢？	
# 50.在创造tulpa期间，使用了哪些方法呢？(冥想塑造（传统方法）)	
# 51.(主动对话)	
# 52.(被动塑造（在干别的事的时候想象tulpa在看）)
# 53.(写设定和故事)	
# 54.(脑补语言动作)	
# 55.(听tulpa冥想音频)	
# 56.(其他)	
# 57.(都没有？)	
# 58.在下列技能中，你们能够做到哪些呢？(描绘（想象出tulpa的样子）)	
# 59.(内投影（拥有幻境且可以在内活动）)	
# 60.(存在感投影（在外界以想象方式看到tulpa）)	
# 61.(视觉投影（在外界以幻觉方式看到能够遮挡背后事物的tulpa）)	
# 62.(附体)	
# 63.(交换)	
# 64.(并行（宿主和tulpa同时思考，且tulpa可以在宿主没想到的时候也能够自己蹦出来）)	
# 65.(记忆屏蔽)	
# 66.(都不会)	
# 67.交换后宿主的状态如何呢？—意识清醒程度（1 表示blackout）	
# 68.思考能力（1 表示算力几乎全归在前台的tulpa，5则反之）	
# 69.后续对交换期间记忆的可读取度	
# 70.后续对交换期间记忆的主观情感认同度	
# 71.在幻境/存在感投影的真实感	
# 72.交换期间处于前/后台对宿主和tulpa的性格影响程度	
# 73.交换后的权限（5表示与交换前等同或更高）	
# 74.交换后自己回到前台的难度	
# 75.在幻境中，下列哪些符合宿主的感受呢？(幻境感觉很真实)	
# 76.(幻境充满各种细节)	
# 77.(幻境可以无限扩展)	
# 78.(在幻境中可以拥有超能力)	
# 79.(幻境可以随心所欲的创造和消灭东西)	
# 80.(第一人称)	
# 81.(第三人称)	
# 82.(幻境是二次元)	
# 83.(幻境是三次元)	
# 84.(幻境环境稳定，不会像ai绘画一样跳动)	
# 85.(幻境是温暖又安全的家)	
# 86.(幻境中藏有无法控制的部分/个体（侵入性意象等）)	
# 87.(幻境会随着情绪和疾病发作而产生变化（如伤心的时候下雨）)	
# 88.(能够进入幻境而忽略大部分现实)	
# 89.(幻境中存在一部分有些微意识、情绪的个体/碎片)	
# 90.(幻境中有一些规则高于你的权限，你无法违反)	
# 91.在幻境中，下列哪些符合tulpa的感受呢？(幻境感觉很真实)	
# 92.(幻境充满各种细节)	
# 93.(幻境可以无限扩展)	
# 94.(在幻境中可以拥有超能力)	
# 95.(幻境可以随心所欲的创造和消灭东西)	
# 96.(第一人称)	
# 97.(第三人称)	
# 98.(幻境是二次元)	
# 99.(幻境是三次元)	
# 100.(幻境环境稳定，不会像ai绘画一样跳动)	
# 101.(幻境是温暖又安全的家)	
# 102.(幻境中藏有无法控制的部分/个体（侵入性意象等）)	
# 103.(幻境会随着情绪和疾病发作而产生变化（如伤心的时候下雨）)	
# 104.(能够进入幻境而忽略大部分现实)	
# 105.(幻境中存在一部分有些微意识、情绪的个体/碎片)	
# 106.(幻境中有一些规则高于你的权限，你无法违反)	
# 107.在投影的时候，tulpa喜欢待在哪里呢？(宿主背着)	
# 108.(宿主肩上)	
# 109.(宿主脑壳里面)	
# 110.(宿主心脏附近)	
# 111.(扒在宿主衣服上)	
# 112.(在旁边走)	
# 113.(在天上飞来飞去)	
# 114.(到处瞬移)	
# 115.(其他)	
# 117.在下列属性中，你的tulpa拥有哪些呢？(完整清晰的外貌和脸)	
# 118.(独特的声线)	
# 119.(独特的思维模式)	
# 120.(数学和逻辑推理能力)	
# 121.(改变幻境的能力)	
# 122.(独有的兴趣或喜好)	
# 123.(安抚宿主的能力)	
# 124.(一定的独立外在人际关系（网上也算）)	
# 125.(长时间交换不难受的能力)	26、(一定程度上能和宿主抗衡的权限)	26、(都没有)	
# 128.宿主和tulpa之间能够传递哪些内容呢？(头压)	
# 129.(t语)	
# 130.(现实语言)	
# 131.(主观情绪（如喜悦）)	
# 132.(主观感觉（如味觉）)	
# 133.(记忆片段)	
# 134.(知识技能)	
# 135.(系统权限)	
# 136.(其他)	
# 137.(都不能？)	
# 138.你和你的tulpa（们）是什么关系呢？(恋人)	
# 139.(夫妻)	
# 140.(好朋友)	
# 141.(兄弟姐妹)	
# 142.(亲子（宿主为父母）)	
# 143.(亲子（宿主为子女）)	
# 144.(泛化的家人关系)	
# 145.(比任何现实关系更为亲近的HT关系)	
# 146.(其他)	
# 147.宿主和tulpa平时会搞不清谁是谁吗？	
# 148.在宿主感到非常难过的时候，tulpa会？(受到抑制难以出来)	
# 149.(和宿主一起抱团难过)	
# 150.(没有太多影响)	
# 151.(交换替宿主分担)	
# 152.(变得活跃清醒并积极安慰宿主)	
# 153.(由于屏蔽，tulpa不知道)	
# 154.(目前没有出现过特别难过的情况)
# 155.(其他)	
# 156.平时会贴贴吗？	
# 157.和没有tulpa的时候相比，宿主感觉tulpa让自己的情绪和生活变得怎么样了呢？	
# 158.(tulpa 回答）你最早的自我记忆是出现在什么时间段呢？	
# 159.宿主对tulpa抱有哪些感情呢？(亲情)	
# 160.(友情)	
# 161.(爱情)	
# 162.(占有欲)	
# 163.(保护欲)	
# 164.(涩涩的感情)	
# 165.(其他)	
# 166.(都没有？)	
# 167.tulpa对宿主抱有哪些感情呢？(亲情)	
# 168.(友情)	
# 169.(爱情)	
# 170.(占有欲)	
# 171.(保护欲)	
# 172.(涩涩的感情)	
# 173.(其他)	
# 174.(都没有？)	
# 175.还有有什么想说的就写到这里吧	
# 176.总分
def read_excel():
    data = pd.read_excel('data.xlsx')
    #源文件
    for index, row in data.iterrows():
        name = row[0]
        # 提取第六个到最后一个单元格（不包含最后一列，因此使用None作为结束索引）
        item = row[6:None].tolist()    
        # 存储结果
        result.append({'name': name, 'item': item})

# 输出结果
print(result)