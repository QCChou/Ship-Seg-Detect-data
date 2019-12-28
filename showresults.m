%fid=fopen('E:\��ҵ���Ľ���\���ݼ�\��������\GoogleEarth\RotationRegionLabels.txt','r');
%fid=fopen('E:\��ҵ���Ľ���\���ݼ�\��������\ˮ��ע\RotationRegionLabels.txt','r');
fid=fopen('E:\���ݼ�\��������\GoogleEarth\RotationRegionLabels.txt','r');
%fid=fopen('E:\���ݼ�\��������\ˮ��ע\RotationRegionLabels.txt','r');

row=0;
while ~feof(fid)
    row=row+sum(fread(fid,10000,'*char')==char(10));
end

row

%rt_img_dir = 'E:\��ҵ���Ľ���\���ݼ�\��������\GoogleEarth\img';
%rt_img_dir = 'E:\��ҵ���Ľ���\���ݼ�\��������\ˮ��ע\label';
rt_img_dir = 'E:\���ݼ�\��������\GoogleEarth\label';
%rt_img_dir = 'E:\���ݼ�\��������\ˮ��ע\label';

frewind(fid);

select = 1:5; %%%%%%%%       to show specified images here
%select = [12 15 21 22 29 33 50]; 
%select = [70]; 
sn = length(select); cnt=1;

for i=1:select(end)
   imgname=fscanf(fid,'%s ',1);
   num=fscanf(fid,'%d ',1); %%%%%
   if i==select(cnt)
      imgpath = fullfile(rt_img_dir,imgname);
      I = imread(imgpath);
      figure,imshow(I);
   end
   for j=1:num
      rectx=fscanf(fid,'%f %f %f %f %f ',5); %%%%%
      recty=fscanf(fid,'%f %f %f %f %f ',5); %%%%%
      cx = fscanf(fid,'%f ',1); 
      cy = fscanf(fid,'%f ',1);  
      w= fscanf(fid,'%f ',1);
      h= fscanf(fid,'%f ',1); 
      theta= fscanf(fid,'%f ',1);     
      if i==select(cnt)
         line(rectx(:),recty(:),'color','y','LineWidth',2);
         hold on, plot(cx,cy,'r+'); text(cx+10,cy+10,[num2str(cx),' ' num2str(cy),' ', num2str(w),' ',num2str(h), ' ',num2str(theta*180/pi)],'Color','white');
      end
   end
   temp=fscanf(fid, '\n');
   if i==select(cnt)
      cnt = cnt+1;
   end
end

fclose(fid);

