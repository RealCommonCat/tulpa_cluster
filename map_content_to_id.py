def ContentToIdx(content):
  match content:
    case '身体的年龄是？	':
         return 1
    case '身体的性别是？	':
         return 2
    case '在目前的T家四分类法中你们属于哪一类呢？(一类)':
         return 3
    case '(二类)	':
         return 4
    case '(三类)	':
         return 5
    case '(四类)	':
         return 6
    case '(不知道t家四分类是什么)	':
         return 7
    case '在埃蒙加德环中，你们认为自己属于哪一类呢？	':
         return 8
    case '在创造第一个tulpa之前，你（们）曾经是？	':
         return 9
    case '你们系统目前拥有多少名成员呢？（包括宿主）	':
         return 10
    case '你们系统中目前有多少名tulpa呢	':
         return 11
    case '在创造第一个tulpa时，身体多少岁呢？	':
         return 12
    case '在创造第一个tulpa时，从开始到成声或者产生可思考的意识花了多久呢（单位:月）（可以问问tulpa本人哦）	':
         return 13
    case '你们加入tulpa社区多久了呢？（单位：月）	':
         return 14
    case '你们系统中最成熟的tulpa活跃度如何呢？	':
         return 15
    case '你们系统中有系魂吗？如果有，那么包括以下哪一种情况呢？(已经放弃系魂认同的前系魂)	':
         return 16
    case '(原创角色系魂)	':
         return 17
    case '(非原创但是脱离原角色的系魂)	':
         return 18
    case '(非原创且没有脱离原角色的系魂)	':
         return 19
    case '(其他)	':
         return 20
    case '(没有系魂)	':
         return 21
    case '你们目前有加入隔壁多意识体社区吗？	':
         return 22
    case '请问你们的身体有哪些精神疾病/症状呢？—轻度抑郁	':
         return 23
    case '中度及以上抑郁	':
         return 24
    case '轻度焦虑	':
         return 25
    case '中度及以上焦虑	':
         return 26
    case '双相情感障碍	':
         return 27
    case '精神分裂症	':
         return 28
    case '强迫症	':
         return 29
    case '孤独症谱系障碍	':
         return 30
    case '注意缺陷多动障碍	':
         return 31
    case '创伤后应激障碍（PTSD）	':
         return 32
    case '复杂型创伤后应激障碍 (C-PTSD)	':
         return 33
    case '分离性身份障碍（DID）	':
         return 34
    case '其他特定分离性障碍（OSDD）（或p-did）	':
         return 35
    case '人格解体/现实解体	':
         return 36
    case '神经衰弱	':
         return 37
    case '请问你们还有上面未提到的精神疾病吗？	':
         return 38
    case '请问你们是从哪里得知tulpa的呢？	':
         return 39
    case '一开始为什么要创造tulpa呢？(需要爱和陪伴)	':
         return 40
    case '(希望有能完全理解自己的人)	':
         return 41
    case '(希望tulpa能够帮助对抗精神疾病)	':
         return 42
    case '(因为喜欢某个角色所以创造了以ta为原型的tulpa)	':
         return 43
    case '(意外创造（当时没有料到tulpa可以有意识）)	':
         return 44
    case '(儿时的幻想朋友)	':
         return 45
    case '(因为朋友/认识的人有)	':
         return 46
    case '(其他)	':
         return 47
    case '在创造tulpa期间，宿主的精神状态总体上如何呢？	':
         return 48
    case '创造tulpa的过程发生在哪里呢？	':
         return 49
    case '在创造tulpa期间，使用了哪些方法呢？(冥想塑造（传统方法）)	':
         return 50
    case '(主动对话)	':
         return 51
    case '(被动塑造（在干别的事的时候想象tulpa在看）)':
         return 52
    case '(写设定和故事)	':
         return 53
    case '(脑补语言动作)	':
         return 54
    case '(听tulpa冥想音频)	':
         return 55
    case '(其他)	':
         return 56
    case '(都没有？)	':
         return 57
    case '在下列技能中，你们能够做到哪些呢？(描绘（想象出tulpa的样子）)	':
         return 58
    case '(内投影（拥有幻境且可以在内活动）)	':
         return 59
    case '(存在感投影（在外界以想象方式看到tulpa）)	':
         return 60
    case '(视觉投影（在外界以幻觉方式看到能够遮挡背后事物的tulpa）)	':
         return 61
    case '(附体)	':
         return 62
    case '(交换)	':
         return 63
    case '(并行（宿主和tulpa同时思考，且tulpa可以在宿主没想到的时候也能够自己蹦出来）)	':
         return 64
    case '(记忆屏蔽)	':
         return 65
    case '(都不会)	':
         return 66
    case '交换后宿主的状态如何呢？—意识清醒程度（1 表示blackout）	':
         return 67
    case '思考能力（1 表示算力几乎全归在前台的tulpa，5则反之）	':
         return 68
    case '后续对交换期间记忆的可读取度	':
         return 69
    case '后续对交换期间记忆的主观情感认同度	':
         return 70
    case '在幻境/存在感投影的真实感	':
         return 71
    case '交换期间处于前/后台对宿主和tulpa的性格影响程度	':
         return 72
    case '交换后的权限（5表示与交换前等同或更高）	':
         return 73
    case '交换后自己回到前台的难度	':
         return 74
    case '在幻境中，下列哪些符合宿主的感受呢？(幻境感觉很真实)	':
         return 75
    case '(幻境充满各种细节)	':
         return 76
    case '(幻境可以无限扩展)	':
         return 77
    case '(在幻境中可以拥有超能力)	':
         return 78
    case '(幻境可以随心所欲的创造和消灭东西)	':
         return 79
    case '(第一人称)	':
         return 80
    case '(第三人称)	':
         return 81
    case '(幻境是二次元)	':
         return 82
    case '(幻境是三次元)	':
         return 83
    case '(幻境环境稳定，不会像ai绘画一样跳动)	':
         return 84
    case '(幻境是温暖又安全的家)	':
         return 85
    case '(幻境中藏有无法控制的部分/个体（侵入性意象等）)	':
         return 86
    case '(幻境会随着情绪和疾病发作而产生变化（如伤心的时候下雨）)	':
         return 87
    case '(能够进入幻境而忽略大部分现实)	':
         return 88
    case '(幻境中存在一部分有些微意识、情绪的个体/碎片)	':
         return 89
    case '(幻境中有一些规则高于你的权限，你无法违反)	':
         return 90
    case '在幻境中，下列哪些符合tulpa的感受呢？(幻境感觉很真实)	':
         return 91
    case '(幻境充满各种细节)	':
         return 92
    case '(幻境可以无限扩展)	':
         return 93
    case '(在幻境中可以拥有超能力)	':
         return 94
    case '(幻境可以随心所欲的创造和消灭东西)	':
         return 95
    case '(第一人称)	':
         return 96
    case '(第三人称)	':
         return 97
    case '(幻境是二次元)	':
         return 98
    case '(幻境是三次元)	':
         return 99
    case '(幻境环境稳定，不会像ai绘画一样跳动)	':
         return 100
    case '(幻境是温暖又安全的家)	':
         return 101
    case '(幻境中藏有无法控制的部分/个体（侵入性意象等）)	':
         return 102
    case '(幻境会随着情绪和疾病发作而产生变化（如伤心的时候下雨）)	':
         return 103
    case '(能够进入幻境而忽略大部分现实)	':
         return 104
    case '(幻境中存在一部分有些微意识、情绪的个体/碎片)	':
         return 105
    case '(幻境中有一些规则高于你的权限，你无法违反)	':
         return 106
    case '在投影的时候，tulpa喜欢待在哪里呢？(宿主背着)	':
         return 107
    case '(宿主肩上)	':
         return 108
    case '(宿主脑壳里面)	':
         return 109
    case '(宿主心脏附近)	':
         return 110
    case '(扒在宿主衣服上)	':
         return 111
    case '(在旁边走)	':
         return 112
    case '(在天上飞来飞去)	':
         return 113
    case '(到处瞬移)	':
         return 114
    case '(其他)	':
         return 115
    case '在下列属性中，你的tulpa拥有哪些呢？(完整清晰的外貌和脸)	':
         return 117
    case '(独特的声线)	':
         return 118
    case '(独特的思维模式)	':
         return 119
    case '(数学和逻辑推理能力)	':
         return 120
    case '(改变幻境的能力)	':
         return 121
    case '(独有的兴趣或喜好)	':
         return 122
    case '(安抚宿主的能力)	':
         return 123
    case '(一定的独立外在人际关系（网上也算）)	':
         return 124
    case '(长时间交换不难受的能力)	26、(一定程度上能和宿主抗衡的权限)	26、(都没有)	':
         return 125
    case '宿主和tulpa之间能够传递哪些内容呢？(头压)	':
         return 128
    case '(t语)	':
         return 129
    case '(现实语言)	':
         return 130
    case '(主观情绪（如喜悦）)	':
         return 131
    case '(主观感觉（如味觉）)	':
         return 132
    case '(记忆片段)	':
         return 133
    case '(知识技能)	':
         return 134
    case '(系统权限)	':
         return 135
    case '(其他)	':
         return 136
    case '(都不能？)	':
         return 137
    case '你和你的tulpa（们）是什么关系呢？(恋人)	':
         return 138
    case '(夫妻)	':
         return 139
    case '(好朋友)	':
         return 140
    case '(兄弟姐妹)	':
         return 141
    case '(亲子（宿主为父母）)	':
         return 142
    case '(亲子（宿主为子女）)	':
         return 143
    case '(泛化的家人关系)	':
         return 144
    case '(比任何现实关系更为亲近的HT关系)	':
         return 145
    case '(其他)	':
         return 146
    case '宿主和tulpa平时会搞不清谁是谁吗？	':
         return 147
    case '在宿主感到非常难过的时候，tulpa会？(受到抑制难以出来)	':
         return 148
    case '(和宿主一起抱团难过)	':
         return 149
    case '(没有太多影响)	':
         return 150
    case '(交换替宿主分担)	':
         return 151
    case '(变得活跃清醒并积极安慰宿主)	':
         return 152
    case '(由于屏蔽，tulpa不知道)	':
         return 153
    case '(目前没有出现过特别难过的情况)':
         return 154
    case '(其他)	':
         return 155
    case '平时会贴贴吗？	':
         return 156
    case '和没有tulpa的时候相比，宿主感觉tulpa让自己的情绪和生活变得怎么样了呢？	':
         return 157
    case '(tulpa 回答）你最早的自我记忆是出现在什么时间段呢？	':
         return 158
    case '宿主对tulpa抱有哪些感情呢？(亲情)	':
         return 159
    case '(友情)	':
         return 160
    case '(爱情)	':
         return 161
    case '(占有欲)	':
         return 162
    case '(保护欲)	':
         return 163
    case '(涩涩的感情)	':
         return 164
    case '(其他)	':
         return 165
    case '(都没有？)	':
         return 166
    case 'tulpa对宿主抱有哪些感情呢？(亲情)	':
         return 167
    case '(友情)	':
         return 168
    case '(爱情)	':
         return 169
    case '(占有欲)	':
         return 170
    case '(保护欲)	':
         return 171
    case '(涩涩的感情)	':
         return 172
    case '(其他)	':
         return 173
    case '(都没有？)	':
         return 174
    case '还有有什么想说的就写到这里吧	':
         return 175
    case '总分':
         return 176
