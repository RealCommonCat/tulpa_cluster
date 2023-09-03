def idxtoContent(idx):
  match idx:
    case 1:
         return '身体的年龄是？	'
    case 2:
         return '身体的性别是？	'
    case 3:
         return '在目前的T家四分类法中你们属于哪一类呢？(一类)'
    case 4:
         return '(二类)	'
    case 5:
         return '(三类)	'
    case 6:
         return '(四类)	'
    case 7:
         return '(不知道t家四分类是什么)	'
    case 8:
         return '在埃蒙加德环中，你们认为自己属于哪一类呢？	'
    case 9:
         return '在创造第一个tulpa之前，你（们）曾经是？	'
    case 10:
         return '你们系统目前拥有多少名成员呢？（包括宿主）	'
    case 11:
         return '你们系统中目前有多少名tulpa呢	'
    case 12:
         return '在创造第一个tulpa时，身体多少岁呢？	'
    case 13:
         return '在创造第一个tulpa时，从开始到成声或者产生可思考的意识花了多久呢（单位:月）（可以问问tulpa本人哦）	'
    case 14:
         return '你们加入tulpa社区多久了呢？（单位：月）	'
    case 15:
         return '你们系统中最成熟的tulpa活跃度如何呢？	'
    case 16:
         return '你们系统中有系魂吗？如果有，那么包括以下哪一种情况呢？(已经放弃系魂认同的前系魂)	'
    case 17:
         return '(原创角色系魂)	'
    case 18:
         return '(非原创但是脱离原角色的系魂)	'
    case 19:
         return '(非原创且没有脱离原角色的系魂)	'
    case 20:
         return '(其他)	'
    case 21:
         return '(没有系魂)	'
    case 22:
         return '你们目前有加入隔壁多意识体社区吗？	'
    case 23:
         return '请问你们的身体有哪些精神疾病/症状呢？—轻度抑郁	'
    case 24:
         return '中度及以上抑郁	'
    case 25:
         return '轻度焦虑	'
    case 26:
         return '中度及以上焦虑	'
    case 27:
         return '双相情感障碍	'
    case 28:
         return '精神分裂症	'
    case 29:
         return '强迫症	'
    case 30:
         return '孤独症谱系障碍	'
    case 31:
         return '注意缺陷多动障碍	'
    case 32:
         return '创伤后应激障碍（PTSD）	'
    case 33:
         return '复杂型创伤后应激障碍 (C-PTSD)	'
    case 34:
         return '分离性身份障碍（DID）	'
    case 35:
         return '其他特定分离性障碍（OSDD）（或p-did）	'
    case 36:
         return '人格解体/现实解体	'
    case 37:
         return '神经衰弱	'
    case 38:
         return '请问你们还有上面未提到的精神疾病吗？	'
    case 39:
         return '请问你们是从哪里得知tulpa的呢？	'
    case 40:
         return '一开始为什么要创造tulpa呢？(需要爱和陪伴)	'
    case 41:
         return '(希望有能完全理解自己的人)	'
    case 42:
         return '(希望tulpa能够帮助对抗精神疾病)	'
    case 43:
         return '(因为喜欢某个角色所以创造了以ta为原型的tulpa)	'
    case 44:
         return '(意外创造（当时没有料到tulpa可以有意识）)	'
    case 45:
         return '(儿时的幻想朋友)	'
    case 46:
         return '(因为朋友/认识的人有)	'
    case 47:
         return '(其他)	'
    case 48:
         return '在创造tulpa期间，宿主的精神状态总体上如何呢？	'
    case 49:
         return '创造tulpa的过程发生在哪里呢？	'
    case 50:
         return '在创造tulpa期间，使用了哪些方法呢？(冥想塑造（传统方法）)	'
    case 51:
         return '(主动对话)	'
    case 52:
         return '(被动塑造（在干别的事的时候想象tulpa在看）)'
    case 53:
         return '(写设定和故事)	'
    case 54:
         return '(脑补语言动作)	'
    case 55:
         return '(听tulpa冥想音频)	'
    case 56:
         return '(其他)	'
    case 57:
         return '(都没有？)	'
    case 58:
         return '在下列技能中，你们能够做到哪些呢？(描绘（想象出tulpa的样子）)	'
    case 59:
         return '(内投影（拥有幻境且可以在内活动）)	'
    case 60:
         return '(存在感投影（在外界以想象方式看到tulpa）)	'
    case 61:
         return '(视觉投影（在外界以幻觉方式看到能够遮挡背后事物的tulpa）)	'
    case 62:
         return '(附体)	'
    case 63:
         return '(交换)	'
    case 64:
         return '(并行（宿主和tulpa同时思考，且tulpa可以在宿主没想到的时候也能够自己蹦出来）)	'
    case 65:
         return '(记忆屏蔽)	'
    case 66:
         return '(都不会)	'
    case 67:
         return '交换后宿主的状态如何呢？—意识清醒程度（1 表示blackout）	'
    case 68:
         return '思考能力（1 表示算力几乎全归在前台的tulpa，5则反之）	'
    case 69:
         return '后续对交换期间记忆的可读取度	'
    case 70:
         return '后续对交换期间记忆的主观情感认同度	'
    case 71:
         return '在幻境/存在感投影的真实感	'
    case 72:
         return '交换期间处于前/后台对宿主和tulpa的性格影响程度	'
    case 73:
         return '交换后的权限（5表示与交换前等同或更高）	'
    case 74:
         return '交换后自己回到前台的难度	'
    case 75:
         return '在幻境中，下列哪些符合宿主的感受呢？(幻境感觉很真实)	'
    case 76:
         return '(幻境充满各种细节)	'
    case 77:
         return '(幻境可以无限扩展)	'
    case 78:
         return '(在幻境中可以拥有超能力)	'
    case 79:
         return '(幻境可以随心所欲的创造和消灭东西)	'
    case 80:
         return '(第一人称)	'
    case 81:
         return '(第三人称)	'
    case 82:
         return '(幻境是二次元)	'
    case 83:
         return '(幻境是三次元)	'
    case 84:
         return '(幻境环境稳定，不会像ai绘画一样跳动)	'
    case 85:
         return '(幻境是温暖又安全的家)	'
    case 86:
         return '(幻境中藏有无法控制的部分/个体（侵入性意象等）)	'
    case 87:
         return '(幻境会随着情绪和疾病发作而产生变化（如伤心的时候下雨）)	'
    case 88:
         return '(能够进入幻境而忽略大部分现实)	'
    case 89:
         return '(幻境中存在一部分有些微意识、情绪的个体/碎片)	'
    case 90:
         return '(幻境中有一些规则高于你的权限，你无法违反)	'
    case 91:
         return '在幻境中，下列哪些符合tulpa的感受呢？(幻境感觉很真实)	'
    case 92:
         return '(幻境充满各种细节)	'
    case 93:
         return '(幻境可以无限扩展)	'
    case 94:
         return '(在幻境中可以拥有超能力)	'
    case 95:
         return '(幻境可以随心所欲的创造和消灭东西)	'
    case 96:
         return '(第一人称)	'
    case 97:
         return '(第三人称)	'
    case 98:
         return '(幻境是二次元)	'
    case 99:
         return '(幻境是三次元)	'
    case 100:
         return '(幻境环境稳定，不会像ai绘画一样跳动)	'
    case 101:
         return '(幻境是温暖又安全的家)	'
    case 102:
         return '(幻境中藏有无法控制的部分/个体（侵入性意象等）)	'
    case 103:
         return '(幻境会随着情绪和疾病发作而产生变化（如伤心的时候下雨）)	'
    case 104:
         return '(能够进入幻境而忽略大部分现实)	'
    case 105:
         return '(幻境中存在一部分有些微意识、情绪的个体/碎片)	'
    case 106:
         return '(幻境中有一些规则高于你的权限，你无法违反)	'
    case 107:
         return '在投影的时候，tulpa喜欢待在哪里呢？(宿主背着)	'
    case 108:
         return '(宿主肩上)	'
    case 109:
         return '(宿主脑壳里面)	'
    case 110:
         return '(宿主心脏附近)	'
    case 111:
         return '(扒在宿主衣服上)	'
    case 112:
         return '(在旁边走)	'
    case 113:
         return '(在天上飞来飞去)	'
    case 114:
         return '(到处瞬移)	'
    case 115:
         return '(其他)	'
    case 116:
         return '在下列属性中，你的tulpa拥有哪些呢？(完整清晰的外貌和脸)	'
    case 117:
         return '(独特的声线)	'
    case 118:
         return '(独特的思维模式)	'
    case 119:
         return '(数学和逻辑推理能力)	'
    case 120:
         return '(改变幻境的能力)	'
    case 121:
         return '(独有的兴趣或喜好)	'
    case 122:
         return '(安抚宿主的能力)	'
    case 123:
         return '(一定的独立外在人际关系（网上也算）)	'
    case 124:
         return '(长时间交换不难受的能力)'	
    case 125:
         return '一定程度上能和宿主抗衡的权限)'
    case 126:
         return '(都没有)	'
    case 127:
         return '宿主和tulpa之间能够传递哪些内容呢？(头压)	'
    case 128:
         return '(t语)	'
    case 129:
         return '(现实语言)	'
    case 130:
         return '(主观情绪（如喜悦）)	'
    case 131:
         return '(主观感觉（如味觉）)	'
    case 132:
         return '(记忆片段)	'
    case 133:
         return '(知识技能)	'
    case 134:
         return '(系统权限)	'
    case 135:
         return '(其他)	'
    case 136:
         return '(都不能？)	'
    case 137:
         return '你和你的tulpa（们）是什么关系呢？(恋人)	'
    case 138:
         return '(夫妻)	'
    case 139:
         return '(好朋友)	'
    case 140:
         return '(兄弟姐妹)	'
    case 141:
         return '(亲子（宿主为父母）)	'
    case 142:
         return '(亲子（宿主为子女）)	'
    case 143:
         return '(泛化的家人关系)	'
    case 144:
         return '(比任何现实关系更为亲近的HT关系)	'
    case 145:
         return '(其他)	'
    case 146:
         return '宿主和tulpa平时会搞不清谁是谁吗？	'
    case 147:
         return '在宿主感到非常难过的时候，tulpa会？(受到抑制难以出来)	'
    case 148:
         return '(和宿主一起抱团难过)	'
    case 149:
         return '(没有太多影响)	'
    case 150:
         return '(交换替宿主分担)	'
    case 151:
         return '(变得活跃清醒并积极安慰宿主)	'
    case 152:
         return '(由于屏蔽，tulpa不知道)	'
    case 153:
         return '(目前没有出现过特别难过的情况)'
    case 154:
         return '(其他)	'
    case 155:
         return '平时会贴贴吗？	'
    case 156:
         return '和没有tulpa的时候相比，宿主感觉tulpa让自己的情绪和生活变得怎么样了呢？	'
    case 157:
         return '(tulpa 回答）你最早的自我记忆是出现在什么时间段呢？	'
    case 158:
         return '宿主对tulpa抱有哪些感情呢？(亲情)	'
    case 159:
         return '(友情)	'
    case 160:
         return '(爱情)	'
    case 161:
         return '(占有欲)	'
    case 162:
         return '(保护欲)	'
    case 163:
         return '(涩涩的感情)	'
    case 164:
         return '(其他)	'
    case 165:
         return '(都没有？)	'
    case 166:
         return 'tulpa对宿主抱有哪些感情呢？(亲情)	'
    case 167:
         return '(友情)	'
    case 168:
         return '(爱情)	'
    case 169:
         return '(占有欲)	'
    case 170:
         return '(保护欲)	'
    case 171:
         return '(涩涩的感情)	'
    case 172:
         return '(其他)	'
    case 173:
         return '(都没有？)	'
    case 174:
         return '还有有什么想说的就写到这里吧	'
    case 175:
         return '总分'
