##1. 写ajax时注意对contenType的设置， charset=utf-， 否者会引发大概率失败发送

##2. ajax POST, 服务器数据没拿到
	
	$.ajax({
		method:"POST",
		url:"/Homework/hand_in",
        data:$("form").serialize(),
		dataType:"json",
		contentType: "application/x-www-form-urlencoded; charset=utf-8",
		success: function(data) {
			if(data["state"]) {
				$("#hint").show().text(data['message']);
			}
			else {
				$("#hint").show().text("文件上传失败");
			}
		}
	});

	.serialize() 对表单呢字段序列化，但是文件流斌没有传上去的

	使用 FormDate(DOM element)
	data: new FormDate($('form'))
	processData设置为false。因为data值是FormData对象，不需要对数据做处理。

<form>标签添加enctype="multipart/form-data"属性。

cache设置为false，上传文件不需要缓存。

contentType设置为false。因为是由<form>表单构造的FormData对象，且已经声明了属性enctype="multipart/form-data"，所以这里设置为false。


##3

os.path.join(BASE_DIR, '/MEDIA').replace('\\', '/')
window 下要加.replace('\\', '/') 把双反斜杠换成正斜杠

##4
下载文件安放得路径重名， django会自动将后者改名， 一般时在后缀之前加“_jjjk” （字符是随意的）
比如 C:/mm.txt, 可能会变成'C:/mm_sydnj.txt'


##5
upload_to配置
 可以指定一个固定的路径，upload_to=' app-name'
 可以指定一个strftime()格式化标签，Django会自动处理成指定格式的日期字符串，如：
file = models.FileField(upload_to="photos/%Y/%m/%d")
则文件存储的时候，会在photos文件夹下，再建立一个文件夹，以年月日命名。
 可以指定一个函数，动态生成存放路径，方法如下， 
class TrainingAttachment(models.Model):
def upload_to(instance, filename):
return '/'.join(['training', instance.subject.name, filename])
subject = models.ForeignKey(TrainingSubject)
file = models.FileField(upload_to=upload_to)
file_name = models.CharField(max_length=255, default='Attachment')
上面代码实现了附件存放到以TrainingSubject.name为目录的路径下。
 可以在上传文件的views处理函数内指定upload_to存放地址
重载通用视图的form_valid方法，重新指定Model的FileField字段的upload_to路径：
def form_valid(self, form):
# 重新指定存放路径
Attachment._meta.get_field('file').upload_to = 'training/'+self.kwargs['subject_pk']
return super(AttachmentCreateView, self).form_valid(form)