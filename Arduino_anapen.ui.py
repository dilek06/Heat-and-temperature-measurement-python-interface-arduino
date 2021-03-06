<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>anapencere</class>
 <widget class="QMainWindow" name="anapencere">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>537</width>
    <height>407</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>300</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1150</width>
    <height>650</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Arduino Arayüz</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>15</x>
      <y>70</y>
      <width>191</width>
      <height>191</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="toolTip">
     <string/>
    </property>
    <property name="frameShape">
     <enum>QFrame::Box</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Sunken</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <widget class="QPushButton" name="portac">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>113</y>
       <width>151</width>
       <height>25</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>50</weight>
       <bold>false</bold>
      </font>
     </property>
     <property name="text">
      <string>Port Aç</string>
     </property>
    </widget>
    <widget class="QPushButton" name="portkapat">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>145</y>
       <width>151</width>
       <height>25</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>50</weight>
       <bold>false</bold>
      </font>
     </property>
     <property name="text">
      <string>Port Kapat</string>
     </property>
    </widget>
    <widget class="QLabel" name="baud">
     <property name="geometry">
      <rect>
       <x>15</x>
       <y>79</y>
       <width>80</width>
       <height>15</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>11</pointsize>
       <weight>50</weight>
       <bold>false</bold>
      </font>
     </property>
     <property name="text">
      <string>Baud Rate</string>
     </property>
    </widget>
    <widget class="QLabel" name="portseciniz">
     <property name="geometry">
      <rect>
       <x>15</x>
       <y>51</y>
       <width>41</width>
       <height>16</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>11</pointsize>
       <weight>50</weight>
       <bold>false</bold>
      </font>
     </property>
     <property name="text">
      <string>Port</string>
     </property>
    </widget>
    <widget class="QComboBox" name="port">
     <property name="geometry">
      <rect>
       <x>100</x>
       <y>46</y>
       <width>70</width>
       <height>22</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>50</weight>
       <bold>false</bold>
      </font>
     </property>
     <property name="currentText">
      <string>COM3</string>
     </property>
     <property name="currentIndex">
      <number>2</number>
     </property>
     <item>
      <property name="text">
       <string>COM1</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM2</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM3</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM4</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM5</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM6</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM7</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM8</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>COM9</string>
      </property>
     </item>
    </widget>
    <widget class="QComboBox" name="baudrate">
     <property name="geometry">
      <rect>
       <x>100</x>
       <y>76</y>
       <width>70</width>
       <height>22</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>50</weight>
       <bold>false</bold>
      </font>
     </property>
     <property name="currentText">
      <string>9600</string>
     </property>
     <property name="currentIndex">
      <number>12</number>
     </property>
     <item>
      <property name="text">
       <string>50</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>75</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>110</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>134</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>150</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>200</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>300</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>600</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>1200</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>1800</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>2400</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>4800</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>9600</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>19200</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>38400</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>57600</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>115200</string>
      </property>
     </item>
    </widget>
    <widget class="QLabel" name="ayarlar">
     <property name="geometry">
      <rect>
       <x>17</x>
       <y>14</y>
       <width>91</width>
       <height>16</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>12</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>AYARLAR</string>
     </property>
    </widget>
   </widget>
   <widget class="QPushButton" name="OFF">
    <property name="geometry">
     <rect>
      <x>525</x>
      <y>277</y>
      <width>42</width>
      <height>23</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>42</width>
      <height>23</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>42</width>
      <height>23</height>
     </size>
    </property>
    <property name="focusPolicy">
     <enum>Qt::StrongFocus</enum>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="autoDefault">
     <bool>false</bool>
    </property>
    <property name="default">
     <bool>false</bool>
    </property>
    <property name="flat">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="RS232">
    <property name="geometry">
     <rect>
      <x>516</x>
      <y>66</y>
      <width>30</width>
      <height>15</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <weight>50</weight>
      <bold>false</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>890</x>
      <y>290</y>
      <width>91</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel
{
  color: rgb(170, 0, 0);
  text-align: center;
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>890</x>
      <y>580</y>
      <width>91</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel
{
  color: rgb(170, 0, 0);
  text-align: center;
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="ruzgarYeksen">
    <property name="geometry">
     <rect>
      <x>599</x>
      <y>420</y>
      <width>71</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel
{
  color: rgb(170, 0, 0);
  text-align: center;
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="pb_cikis">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>300</y>
      <width>130</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton:pressed {
    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1,   stop:0 rgba(225,225,225, 255), stop:1 rgba(210,180,140, 255))
}
QPushButton {
     background-color: rgb(225,225,225); border: 2px solid rgb(173,173,173);
     border-radius: 10px;
     color: rgb(50,50,50);
}

QPushButton:disabled {
    background-color: rgb(225,225,225)
}</string>
    </property>
    <property name="text">
     <string>ÇIKIŞ</string>
    </property>
   </widget>
   <widget class="QFrame" name="frame_2">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>20</y>
      <width>261</width>
      <height>341</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::Box</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Sunken</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <widget class="QProgressBar" name="progressBar_1">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>50</y>
       <width>21</width>
       <height>250</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar {
     border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);
 }

 QProgressBar::chunk {
     background-color: rgb(255, 0, 0);
 }</string>
     </property>
     <property name="value">
      <number>1</number>
     </property>
     <property name="alignment">
      <set>Qt::AlignBottom|Qt::AlignHCenter</set>
     </property>
     <property name="textVisible">
      <bool>false</bool>
     </property>
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="invertedAppearance">
      <bool>false</bool>
     </property>
     <property name="textDirection">
      <enum>QProgressBar::BottomToTop</enum>
     </property>
    </widget>
    <widget class="QProgressBar" name="progressBar_2">
     <property name="geometry">
      <rect>
       <x>182</x>
       <y>50</y>
       <width>21</width>
       <height>250</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar {
     border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);
 }

 QProgressBar::chunk {
     background-color: rgb(85, 255, 255);
 }</string>
     </property>
     <property name="value">
      <number>1</number>
     </property>
     <property name="alignment">
      <set>Qt::AlignBottom|Qt::AlignHCenter</set>
     </property>
     <property name="textVisible">
      <bool>false</bool>
     </property>
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="invertedAppearance">
      <bool>false</bool>
     </property>
     <property name="textDirection">
      <enum>QProgressBar::BottomToTop</enum>
     </property>
    </widget>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>32</x>
       <y>310</y>
       <width>60</width>
       <height>20</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>12</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>ISI (C)</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>154</x>
       <y>310</y>
       <width>80</width>
       <height>16</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>12</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>NEM (%)</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="label_5">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>10</y>
       <width>60</width>
       <height>30</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel

 {
	 border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);
 }</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="label_6">
     <property name="geometry">
      <rect>
       <x>161</x>
       <y>10</y>
       <width>60</width>
       <height>30</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>11</pointsize>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel

 {
	 border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);
 }</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="label_8">
     <property name="geometry">
      <rect>
       <x>95</x>
       <y>43</y>
       <width>60</width>
       <height>275</height>
      </rect>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="pixmap">
      <pixmap>Scale.jpg</pixmap>
     </property>
     <property name="scaledContents">
      <bool>true</bool>
     </property>
    </widget>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>22</y>
      <width>181</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>11</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel

 {
	 border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);
 }</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>537</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>pb_cikis</sender>
   <signal>clicked()</signal>
   <receiver>anapencere</receiver>
   <slot>close()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>151</x>
     <y>338</y>
    </hint>
    <hint type="destinationlabel">
     <x>205</x>
     <y>371</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>