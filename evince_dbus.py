<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>gedit-plugins - Collection of plugins for the gedit Text Editor</title>
<meta name='generator' content='cgit v0.10.1'/>
<meta name='robots' content='index, nofollow'/>
<link rel='stylesheet' type='text/css' href='/browse/cgit-gnome.css'/>
<link rel='shortcut icon' href='https://static.gnome.org/img/logo/foot-16.png'/>
<link rel='alternate' title='Atom feed' href='https://git.gnome.org/browse/gedit-plugins/atom/plugins/synctex/synctex/evince_dbus.py?h=master' type='application/atom+xml'/>
</head>
<body>
<div id="global_domain_bar">
<div class="maxwidth">
	<div class="tab">
	<a class="root" href="https://www.gnome.org/">GNOME.org</a>
	</div>
</div>
</div>

<div id="page">
    <div id="logo_bar" class="container_12">
      <div id="logo" class="grid_3">
        <a title="Go to home page" href="https://git.gnome.org/"><img src="https://static.gnome.org/img/gnome-git.png" alt="GNOME: Git Repository" /></a>
      </div>

      <div id="top_bar" class="grid_9">
        <div class="left">
          <div class="menu-globalnav-container">
            <ul id="menu-globalnav" class="menu">
              <li id="menu-item-1039" class=
              "menu-item menu-item-type-post_type menu-item-object-page menu-item-1039">
              <a href="https://git.gnome.org/">Home</a></li>

              <li id="menu-item-1037" class=
              "menu-item menu-item-type-post_type menu-item-object-page menu-item-1037">
              <a href="https://wiki.gnome.org/Git">Git Help</a></li>
            </ul>
          </div>
        </div>
      </div>
      
    </div>
</div>
<div id='cgit'><table id='header'>
<tr>
<td class='main'><a href='/browse/'>index</a> : <a title='gedit-plugins' href='/browse/gedit-plugins/'>gedit-plugins</a></td><td class='form'><form method='get' action=''>
<select name='h' onchange='this.form.submit();'>
<option value='dashboard2'>dashboard2</option>
<option value='emacsyindent'>emacsyindent</option>
<option value='gnome-2-18'>gnome-2-18</option>
<option value='gnome-2-22'>gnome-2-22</option>
<option value='gnome-2-26'>gnome-2-26</option>
<option value='gnome-2-28'>gnome-2-28</option>
<option value='gnome-2-30'>gnome-2-30</option>
<option value='gnome-2-32'>gnome-2-32</option>
<option value='gnome-3-0'>gnome-3-0</option>
<option value='gnome-3-10'>gnome-3-10</option>
<option value='gnome-3-12'>gnome-3-12</option>
<option value='gnome-3-2'>gnome-3-2</option>
<option value='gnome-3-4'>gnome-3-4</option>
<option value='gnome-3-6'>gnome-3-6</option>
<option value='gnome-3-8'>gnome-3-8</option>
<option value='libgpe'>libgpe</option>
<option value='master' selected='selected'>master</option>
<option value='old_plugins'>old_plugins</option>
<option value='wip/python3'>wip/python3</option>
<option value='wip/redesign'>wip/redesign</option>
<option value='wip/rpm-plugin'>wip/rpm-plugin</option>
</select> <input type='submit' name='' value='switch'/></form></td></tr>
<tr><td class='sub'>Collection of plugins for the gedit Text Editor</td><td class='sub right'></td></tr></table>
<table class='tabs'><tr><td>
<a href='/browse/gedit-plugins/'>summary</a><a href='/browse/gedit-plugins/refs/'>refs</a><a href='/browse/gedit-plugins/log/plugins/synctex/synctex/evince_dbus.py'>log</a><a class='active' href='/browse/gedit-plugins/tree/plugins/synctex/synctex/evince_dbus.py'>tree</a><a href='/browse/gedit-plugins/commit/plugins/synctex/synctex/evince_dbus.py'>commit</a><a href='/browse/gedit-plugins/diff/plugins/synctex/synctex/evince_dbus.py'>diff</a><a href='/browse/gedit-plugins/stats/plugins/synctex/synctex/evince_dbus.py'>stats</a></td><td class='form'><form class='right' method='get' action='/browse/gedit-plugins/log/plugins/synctex/synctex/evince_dbus.py'>
<select name='qt'>
<option value='grep'>log msg</option>
<option value='author'>author</option>
<option value='committer'>committer</option>
<option value='range'>range</option>
</select>
<input class='txt' type='text' size='10' name='q' value=''/>
<input type='submit' value='search'/>
</form>
</td></tr></table>
<div class='path'>path: <a href='/browse/gedit-plugins/tree/'>root</a>/<a href='/browse/gedit-plugins/tree/plugins'>plugins</a>/<a href='/browse/gedit-plugins/tree/plugins/synctex'>synctex</a>/<a href='/browse/gedit-plugins/tree/plugins/synctex/synctex'>synctex</a>/<a href='/browse/gedit-plugins/tree/plugins/synctex/synctex/evince_dbus.py'>evince_dbus.py</a></div><div class='content'>blob: ba6aaeaef7fe30ddfb68b44d14ca2d47d7b20553 (<a href='/browse/gedit-plugins/plain/plugins/synctex/synctex/evince_dbus.py'>plain</a>)
<table summary='blob content' class='blob'>
<tr><td class='linenumbers'><pre><a id='n1' href='#n1'>1</a>
<a id='n2' href='#n2'>2</a>
<a id='n3' href='#n3'>3</a>
<a id='n4' href='#n4'>4</a>
<a id='n5' href='#n5'>5</a>
<a id='n6' href='#n6'>6</a>
<a id='n7' href='#n7'>7</a>
<a id='n8' href='#n8'>8</a>
<a id='n9' href='#n9'>9</a>
<a id='n10' href='#n10'>10</a>
<a id='n11' href='#n11'>11</a>
<a id='n12' href='#n12'>12</a>
<a id='n13' href='#n13'>13</a>
<a id='n14' href='#n14'>14</a>
<a id='n15' href='#n15'>15</a>
<a id='n16' href='#n16'>16</a>
<a id='n17' href='#n17'>17</a>
<a id='n18' href='#n18'>18</a>
<a id='n19' href='#n19'>19</a>
<a id='n20' href='#n20'>20</a>
<a id='n21' href='#n21'>21</a>
<a id='n22' href='#n22'>22</a>
<a id='n23' href='#n23'>23</a>
<a id='n24' href='#n24'>24</a>
<a id='n25' href='#n25'>25</a>
<a id='n26' href='#n26'>26</a>
<a id='n27' href='#n27'>27</a>
<a id='n28' href='#n28'>28</a>
<a id='n29' href='#n29'>29</a>
<a id='n30' href='#n30'>30</a>
<a id='n31' href='#n31'>31</a>
<a id='n32' href='#n32'>32</a>
<a id='n33' href='#n33'>33</a>
<a id='n34' href='#n34'>34</a>
<a id='n35' href='#n35'>35</a>
<a id='n36' href='#n36'>36</a>
<a id='n37' href='#n37'>37</a>
<a id='n38' href='#n38'>38</a>
<a id='n39' href='#n39'>39</a>
<a id='n40' href='#n40'>40</a>
<a id='n41' href='#n41'>41</a>
<a id='n42' href='#n42'>42</a>
<a id='n43' href='#n43'>43</a>
<a id='n44' href='#n44'>44</a>
<a id='n45' href='#n45'>45</a>
<a id='n46' href='#n46'>46</a>
<a id='n47' href='#n47'>47</a>
<a id='n48' href='#n48'>48</a>
<a id='n49' href='#n49'>49</a>
<a id='n50' href='#n50'>50</a>
<a id='n51' href='#n51'>51</a>
<a id='n52' href='#n52'>52</a>
<a id='n53' href='#n53'>53</a>
<a id='n54' href='#n54'>54</a>
<a id='n55' href='#n55'>55</a>
<a id='n56' href='#n56'>56</a>
<a id='n57' href='#n57'>57</a>
<a id='n58' href='#n58'>58</a>
<a id='n59' href='#n59'>59</a>
<a id='n60' href='#n60'>60</a>
<a id='n61' href='#n61'>61</a>
<a id='n62' href='#n62'>62</a>
<a id='n63' href='#n63'>63</a>
<a id='n64' href='#n64'>64</a>
<a id='n65' href='#n65'>65</a>
<a id='n66' href='#n66'>66</a>
<a id='n67' href='#n67'>67</a>
<a id='n68' href='#n68'>68</a>
<a id='n69' href='#n69'>69</a>
<a id='n70' href='#n70'>70</a>
<a id='n71' href='#n71'>71</a>
<a id='n72' href='#n72'>72</a>
<a id='n73' href='#n73'>73</a>
<a id='n74' href='#n74'>74</a>
<a id='n75' href='#n75'>75</a>
<a id='n76' href='#n76'>76</a>
<a id='n77' href='#n77'>77</a>
<a id='n78' href='#n78'>78</a>
<a id='n79' href='#n79'>79</a>
<a id='n80' href='#n80'>80</a>
<a id='n81' href='#n81'>81</a>
<a id='n82' href='#n82'>82</a>
<a id='n83' href='#n83'>83</a>
<a id='n84' href='#n84'>84</a>
<a id='n85' href='#n85'>85</a>
<a id='n86' href='#n86'>86</a>
<a id='n87' href='#n87'>87</a>
<a id='n88' href='#n88'>88</a>
<a id='n89' href='#n89'>89</a>
<a id='n90' href='#n90'>90</a>
<a id='n91' href='#n91'>91</a>
<a id='n92' href='#n92'>92</a>
<a id='n93' href='#n93'>93</a>
<a id='n94' href='#n94'>94</a>
<a id='n95' href='#n95'>95</a>
<a id='n96' href='#n96'>96</a>
<a id='n97' href='#n97'>97</a>
<a id='n98' href='#n98'>98</a>
<a id='n99' href='#n99'>99</a>
<a id='n100' href='#n100'>100</a>
<a id='n101' href='#n101'>101</a>
<a id='n102' href='#n102'>102</a>
<a id='n103' href='#n103'>103</a>
<a id='n104' href='#n104'>104</a>
<a id='n105' href='#n105'>105</a>
<a id='n106' href='#n106'>106</a>
<a id='n107' href='#n107'>107</a>
<a id='n108' href='#n108'>108</a>
<a id='n109' href='#n109'>109</a>
<a id='n110' href='#n110'>110</a>
<a id='n111' href='#n111'>111</a>
<a id='n112' href='#n112'>112</a>
<a id='n113' href='#n113'>113</a>
<a id='n114' href='#n114'>114</a>
<a id='n115' href='#n115'>115</a>
<a id='n116' href='#n116'>116</a>
<a id='n117' href='#n117'>117</a>
<a id='n118' href='#n118'>118</a>
<a id='n119' href='#n119'>119</a>
<a id='n120' href='#n120'>120</a>
<a id='n121' href='#n121'>121</a>
<a id='n122' href='#n122'>122</a>
<a id='n123' href='#n123'>123</a>
<a id='n124' href='#n124'>124</a>
<a id='n125' href='#n125'>125</a>
<a id='n126' href='#n126'>126</a>
<a id='n127' href='#n127'>127</a>
<a id='n128' href='#n128'>128</a>
<a id='n129' href='#n129'>129</a>
<a id='n130' href='#n130'>130</a>
<a id='n131' href='#n131'>131</a>
<a id='n132' href='#n132'>132</a>
<a id='n133' href='#n133'>133</a>
<a id='n134' href='#n134'>134</a>
<a id='n135' href='#n135'>135</a>
<a id='n136' href='#n136'>136</a>
<a id='n137' href='#n137'>137</a>
<a id='n138' href='#n138'>138</a>
<a id='n139' href='#n139'>139</a>
<a id='n140' href='#n140'>140</a>
<a id='n141' href='#n141'>141</a>
<a id='n142' href='#n142'>142</a>
<a id='n143' href='#n143'>143</a>
<a id='n144' href='#n144'>144</a>
<a id='n145' href='#n145'>145</a>
<a id='n146' href='#n146'>146</a>
<a id='n147' href='#n147'>147</a>
<a id='n148' href='#n148'>148</a>
<a id='n149' href='#n149'>149</a>
<a id='n150' href='#n150'>150</a>
<a id='n151' href='#n151'>151</a>
<a id='n152' href='#n152'>152</a>
<a id='n153' href='#n153'>153</a>
<a id='n154' href='#n154'>154</a>
<a id='n155' href='#n155'>155</a>
<a id='n156' href='#n156'>156</a>
<a id='n157' href='#n157'>157</a>
<a id='n158' href='#n158'>158</a>
<a id='n159' href='#n159'>159</a>
<a id='n160' href='#n160'>160</a>
<a id='n161' href='#n161'>161</a>
<a id='n162' href='#n162'>162</a>
<a id='n163' href='#n163'>163</a>
<a id='n164' href='#n164'>164</a>
<a id='n165' href='#n165'>165</a>
<a id='n166' href='#n166'>166</a>
<a id='n167' href='#n167'>167</a>
<a id='n168' href='#n168'>168</a>
<a id='n169' href='#n169'>169</a>
<a id='n170' href='#n170'>170</a>
<a id='n171' href='#n171'>171</a>
<a id='n172' href='#n172'>172</a>
<a id='n173' href='#n173'>173</a>
<a id='n174' href='#n174'>174</a>
<a id='n175' href='#n175'>175</a>
<a id='n176' href='#n176'>176</a>
<a id='n177' href='#n177'>177</a>
<a id='n178' href='#n178'>178</a>
<a id='n179' href='#n179'>179</a>
<a id='n180' href='#n180'>180</a>
<a id='n181' href='#n181'>181</a>
<a id='n182' href='#n182'>182</a>
<a id='n183' href='#n183'>183</a>
<a id='n184' href='#n184'>184</a>
<a id='n185' href='#n185'>185</a>
<a id='n186' href='#n186'>186</a>
<a id='n187' href='#n187'>187</a>
</pre></td>
<td class='lines'><pre><code><span class="hl slc">#!/usr/bin/python</span>
<span class="hl slc"># -*- coding: utf-8 -*-</span>

<span class="hl slc"># This file is part of the Gedit Synctex plugin.</span>
<span class="hl slc">#</span>
<span class="hl slc"># Copyright (C) 2010 Jose Aliste &lt;jose.aliste&#64;gmail.com&gt;</span>
<span class="hl slc">#</span>
<span class="hl slc"># This program is free software; you can redistribute it and/or modify it under</span>
<span class="hl slc"># the terms of the GNU General Public Licence as published by the Free Software</span>
<span class="hl slc"># Foundation; either version 2 of the Licence, or (at your option) any later</span>
<span class="hl slc"># version.</span>
<span class="hl slc">#</span>
<span class="hl slc"># This program is distributed in the hope that it will be useful, but WITHOUT</span>
<span class="hl slc"># ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS</span>
<span class="hl slc"># FOR A PARTICULAR PURPOSE.  See the GNU General Public Licence for more</span>
<span class="hl slc"># details.</span>
<span class="hl slc">#</span>
<span class="hl slc"># You should have received a copy of the GNU General Public Licence along with</span>
<span class="hl slc"># this program; if not, write to the Free Software Foundation, Inc., 51 Franklin</span>
<span class="hl slc"># Street, Fifth Floor, Boston, MA  02110-1301, USA</span>

<span class="hl kwa">import</span> dbus<span class="hl opt">,</span> subprocess<span class="hl opt">,</span> time

RUNNING<span class="hl opt">,</span> CLOSED <span class="hl opt">=</span> <span class="hl kwb">range</span><span class="hl opt">(</span><span class="hl num">2</span><span class="hl opt">)</span>

EV_DAEMON_PATH <span class="hl opt">=</span> <span class="hl str">&quot;/org/gnome/evince/Daemon&quot;</span>
EV_DAEMON_NAME <span class="hl opt">=</span> <span class="hl str">&quot;org.gnome.evince.Daemon&quot;</span>
EV_DAEMON_IFACE <span class="hl opt">=</span> <span class="hl str">&quot;org.gnome.evince.Daemon&quot;</span>

EVINCE_PATH <span class="hl opt">=</span> <span class="hl str">&quot;/org/gnome/evince/Evince&quot;</span>
EVINCE_IFACE <span class="hl opt">=</span> <span class="hl str">&quot;org.gnome.evince.Application&quot;</span>

EV_WINDOW_IFACE <span class="hl opt">=</span> <span class="hl str">&quot;org.gnome.evince.Window&quot;</span>



<span class="hl kwa">class</span> EvinceWindowProxy<span class="hl opt">:</span>
    <span class="hl str">&quot;&quot;&quot;A DBUS proxy for an Evince Window.&quot;&quot;&quot;</span>
    daemon <span class="hl opt">=</span> <span class="hl kwa">None</span>
    bus <span class="hl opt">=</span> <span class="hl kwa">None</span>

    <span class="hl kwa">def</span> <span class="hl kwd">__init__</span><span class="hl opt">(</span>self<span class="hl opt">,</span> uri<span class="hl opt">,</span> spawn <span class="hl opt">=</span> <span class="hl kwa">False</span><span class="hl opt">,</span> logger <span class="hl opt">=</span> <span class="hl kwa">None</span><span class="hl opt">):</span>
        self<span class="hl opt">.</span>_log <span class="hl opt">=</span> logger
        self<span class="hl opt">.</span>uri <span class="hl opt">=</span> uri
        self<span class="hl opt">.</span>spawn <span class="hl opt">=</span> spawn
        self<span class="hl opt">.</span>status <span class="hl opt">=</span> CLOSED
        self<span class="hl opt">.</span>source_handler <span class="hl opt">=</span> <span class="hl kwa">None</span>
        self<span class="hl opt">.</span>dbus_name <span class="hl opt">=</span> <span class="hl str">''</span>
        self<span class="hl opt">.</span>_handler <span class="hl opt">=</span> <span class="hl kwa">None</span>
        <span class="hl kwa">try</span><span class="hl opt">:</span>
            <span class="hl kwa">if</span> EvinceWindowProxy<span class="hl opt">.</span>bus <span class="hl kwa">is None</span><span class="hl opt">:</span>
                EvinceWindowProxy<span class="hl opt">.</span>bus <span class="hl opt">=</span> dbus<span class="hl opt">.</span><span class="hl kwd">SessionBus</span><span class="hl opt">()</span>

            <span class="hl kwa">if</span> EvinceWindowProxy<span class="hl opt">.</span>daemon <span class="hl kwa">is None</span><span class="hl opt">:</span>
                EvinceWindowProxy<span class="hl opt">.</span>daemon <span class="hl opt">=</span> EvinceWindowProxy<span class="hl opt">.</span>bus<span class="hl opt">.</span><span class="hl kwd">get_object</span><span class="hl opt">(</span>EV_DAEMON_NAME<span class="hl opt">,</span>
                                                EV_DAEMON_PATH<span class="hl opt">,</span>
                                                follow_name_owner_changes<span class="hl opt">=</span><span class="hl kwa">True</span><span class="hl opt">)</span>
            EvinceWindowProxy<span class="hl opt">.</span>bus<span class="hl opt">.</span><span class="hl kwd">add_signal_receiver</span><span class="hl opt">(</span>self<span class="hl opt">.</span>_on_doc_loaded<span class="hl opt">,</span> signal_name<span class="hl opt">=</span><span class="hl str">&quot;DocumentLoaded&quot;</span><span class="hl opt">,</span> 
                                                      dbus_interface <span class="hl opt">=</span> EV_WINDOW_IFACE<span class="hl opt">,</span> 
                                                      sender_keyword<span class="hl opt">=</span><span class="hl str">'sender'</span><span class="hl opt">)</span>
            self<span class="hl opt">.</span><span class="hl kwd">_get_dbus_name</span><span class="hl opt">(</span><span class="hl kwa">False</span><span class="hl opt">)</span>

        <span class="hl kwa">except</span> dbus<span class="hl opt">.</span>DBusException<span class="hl opt">:</span>
            <span class="hl kwa">if</span> self<span class="hl opt">.</span>_log<span class="hl opt">:</span>
                self<span class="hl opt">.</span>_log<span class="hl opt">.</span><span class="hl kwd">debug</span><span class="hl opt">(</span><span class="hl str">&quot;Could not connect to the Evince Daemon&quot;</span><span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">_on_doc_loaded</span><span class="hl opt">(</span>self<span class="hl opt">,</span> uri<span class="hl opt">, **</span>keyargs<span class="hl opt">):</span>
        <span class="hl kwa">if</span> uri <span class="hl opt">==</span> self<span class="hl opt">.</span>uri <span class="hl kwa">and</span> self<span class="hl opt">.</span>_handler <span class="hl kwa">is None</span><span class="hl opt">:</span>
            self<span class="hl opt">.</span><span class="hl kwd">handle_find_document_reply</span><span class="hl opt">(</span>keyargs<span class="hl opt">[</span><span class="hl str">'sender'</span><span class="hl opt">])</span>
        
    <span class="hl kwa">def</span> <span class="hl kwd">_get_dbus_name</span><span class="hl opt">(</span>self<span class="hl opt">,</span> spawn<span class="hl opt">):</span>
        EvinceWindowProxy<span class="hl opt">.</span>daemon<span class="hl opt">.</span><span class="hl kwd">FindDocument</span><span class="hl opt">(</span>self<span class="hl opt">.</span>uri<span class="hl opt">,</span>spawn<span class="hl opt">,</span>
                     reply_handler<span class="hl opt">=</span>self<span class="hl opt">.</span>handle_find_document_reply<span class="hl opt">,</span>
                     error_handler<span class="hl opt">=</span>self<span class="hl opt">.</span>handle_find_document_error<span class="hl opt">,</span>
                     dbus_interface <span class="hl opt">=</span> EV_DAEMON_IFACE<span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">handle_find_document_error</span><span class="hl opt">(</span>self<span class="hl opt">,</span> error<span class="hl opt">):</span>
        <span class="hl kwa">if</span> self<span class="hl opt">.</span>_log<span class="hl opt">:</span>
            self<span class="hl opt">.</span>_log<span class="hl opt">.</span><span class="hl kwd">debug</span><span class="hl opt">(</span><span class="hl str">&quot;FindDocument DBus call has failed&quot;</span><span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">handle_find_document_reply</span><span class="hl opt">(</span>self<span class="hl opt">,</span> evince_name<span class="hl opt">):</span>
        <span class="hl kwa">if</span> self<span class="hl opt">.</span>_handler <span class="hl kwa">is not None</span><span class="hl opt">:</span>
            handler <span class="hl opt">=</span> self<span class="hl opt">.</span>_handler
        <span class="hl kwa">else</span><span class="hl opt">:</span>
            handler <span class="hl opt">=</span> self<span class="hl opt">.</span>handle_get_window_list_reply
        <span class="hl kwa">if</span> evince_name <span class="hl opt">!=</span> <span class="hl str">''</span><span class="hl opt">:</span>
            self<span class="hl opt">.</span>dbus_name <span class="hl opt">=</span> evince_name
            self<span class="hl opt">.</span>status <span class="hl opt">=</span> RUNNING
            self<span class="hl opt">.</span>evince <span class="hl opt">=</span> EvinceWindowProxy<span class="hl opt">.</span>bus<span class="hl opt">.</span><span class="hl kwd">get_object</span><span class="hl opt">(</span>self<span class="hl opt">.</span>dbus_name<span class="hl opt">,</span> EVINCE_PATH<span class="hl opt">)</span>
            self<span class="hl opt">.</span>evince<span class="hl opt">.</span><span class="hl kwd">GetWindowList</span><span class="hl opt">(</span>dbus_interface <span class="hl opt">=</span> EVINCE_IFACE<span class="hl opt">,</span>
                          reply_handler <span class="hl opt">=</span> handler<span class="hl opt">,</span>
                          error_handler <span class="hl opt">=</span> self<span class="hl opt">.</span>handle_get_window_list_error<span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">handle_get_window_list_error</span> <span class="hl opt">(</span>self<span class="hl opt">,</span> e<span class="hl opt">):</span>
        <span class="hl kwa">if</span> self<span class="hl opt">.</span>_log<span class="hl opt">:</span>
            self<span class="hl opt">.</span>_log<span class="hl opt">.</span><span class="hl kwd">debug</span><span class="hl opt">(</span><span class="hl str">&quot;GetWindowList DBus call has failed&quot;</span><span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">handle_get_window_list_reply</span> <span class="hl opt">(</span>self<span class="hl opt">,</span> window_list<span class="hl opt">):</span>
        <span class="hl kwa">if</span> <span class="hl kwb">len</span><span class="hl opt">(</span>window_list<span class="hl opt">) &gt;</span> <span class="hl num">0</span><span class="hl opt">:</span>
            window_obj <span class="hl opt">=</span> EvinceWindowProxy<span class="hl opt">.</span>bus<span class="hl opt">.</span><span class="hl kwd">get_object</span><span class="hl opt">(</span>self<span class="hl opt">.</span>dbus_name<span class="hl opt">,</span> window_list<span class="hl opt">[</span><span class="hl num">0</span><span class="hl opt">])</span>
            self<span class="hl opt">.</span>window <span class="hl opt">=</span> dbus<span class="hl opt">.</span><span class="hl kwd">Interface</span><span class="hl opt">(</span>window_obj<span class="hl opt">,</span>EV_WINDOW_IFACE<span class="hl opt">)</span>
            self<span class="hl opt">.</span>window<span class="hl opt">.</span><span class="hl kwd">connect_to_signal</span><span class="hl opt">(</span><span class="hl str">&quot;Closed&quot;</span><span class="hl opt">,</span> self<span class="hl opt">.</span>on_window_close<span class="hl opt">)</span>
            self<span class="hl opt">.</span>window<span class="hl opt">.</span><span class="hl kwd">connect_to_signal</span><span class="hl opt">(</span><span class="hl str">&quot;SyncSource&quot;</span><span class="hl opt">,</span> self<span class="hl opt">.</span>on_sync_source<span class="hl opt">)</span>
        <span class="hl kwa">else</span><span class="hl opt">:</span>
            <span class="hl slc">#That should never happen. </span>
            <span class="hl kwa">if</span> self<span class="hl opt">.</span>_log<span class="hl opt">:</span>
                self<span class="hl opt">.</span>_log<span class="hl opt">.</span><span class="hl kwd">debug</span><span class="hl opt">(</span><span class="hl str">&quot;GetWindowList returned empty list&quot;</span><span class="hl opt">)</span>


    <span class="hl kwa">def</span> <span class="hl kwd">set_source_handler</span> <span class="hl opt">(</span>self<span class="hl opt">,</span> source_handler<span class="hl opt">):</span>
        self<span class="hl opt">.</span>source_handler <span class="hl opt">=</span> source_handler

    <span class="hl kwa">def</span> <span class="hl kwd">on_window_close</span><span class="hl opt">(</span>self<span class="hl opt">):</span>
        self<span class="hl opt">.</span>window <span class="hl opt">=</span> <span class="hl kwa">None</span>
        self<span class="hl opt">.</span>status <span class="hl opt">=</span> CLOSED

    <span class="hl kwa">def</span> <span class="hl kwd">on_sync_source</span><span class="hl opt">(</span>self<span class="hl opt">,</span> input_file<span class="hl opt">,</span> source_link<span class="hl opt">,</span> timestamp<span class="hl opt">):</span>
        <span class="hl kwa">if</span> self<span class="hl opt">.</span>source_handler <span class="hl kwa">is not None</span><span class="hl opt">:</span>
            self<span class="hl opt">.</span><span class="hl kwd">source_handler</span><span class="hl opt">(</span>input_file<span class="hl opt">,</span> source_link<span class="hl opt">,</span> timestamp<span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">SyncView</span><span class="hl opt">(</span>self<span class="hl opt">,</span> input_file<span class="hl opt">,</span> data<span class="hl opt">,</span> time<span class="hl opt">):</span>
        <span class="hl kwa">if</span> self<span class="hl opt">.</span>status <span class="hl opt">==</span> CLOSED<span class="hl opt">:</span>
            <span class="hl kwa">if</span> self<span class="hl opt">.</span>spawn<span class="hl opt">:</span>
                self<span class="hl opt">.</span>_tmp_syncview <span class="hl opt">= [</span>input_file<span class="hl opt">,</span> data<span class="hl opt">,</span> time<span class="hl opt">];</span>
                self<span class="hl opt">.</span>_handler <span class="hl opt">=</span> self<span class="hl opt">.</span>_syncview_handler
                self<span class="hl opt">.</span><span class="hl kwd">_get_dbus_name</span><span class="hl opt">(</span><span class="hl kwa">True</span><span class="hl opt">)</span>
        <span class="hl kwa">else</span><span class="hl opt">:</span>
            self<span class="hl opt">.</span>window<span class="hl opt">.</span><span class="hl kwd">SyncView</span><span class="hl opt">(</span>input_file<span class="hl opt">,</span> data<span class="hl opt">,</span> time<span class="hl opt">,</span>  dbus_interface <span class="hl opt">=</span> <span class="hl str">&quot;org.gnome.evince.Window&quot;</span><span class="hl opt">)</span>

    <span class="hl kwa">def</span> <span class="hl kwd">_syncview_handler</span><span class="hl opt">(</span>self<span class="hl opt">,</span> window_list<span class="hl opt">):</span>
        self<span class="hl opt">.</span><span class="hl kwd">handle_get_window_list_reply</span><span class="hl opt">(</span>window_list<span class="hl opt">)</span>

        <span class="hl kwa">if</span> self<span class="hl opt">.</span>status <span class="hl opt">==</span> CLOSED<span class="hl opt">:</span> 
            <span class="hl kwa">return False</span>
        self<span class="hl opt">.</span>window<span class="hl opt">.</span><span class="hl kwd">SyncView</span><span class="hl opt">(</span>self<span class="hl opt">.</span>_tmp_syncview<span class="hl opt">[</span><span class="hl num">0</span><span class="hl opt">],</span>self<span class="hl opt">.</span>_tmp_syncview<span class="hl opt">[</span><span class="hl num">1</span><span class="hl opt">],</span> self<span class="hl opt">.</span>_tmp_syncview<span class="hl opt">[</span><span class="hl num">2</span><span class="hl opt">],</span> dbus_interface<span class="hl opt">=</span><span class="hl str">&quot;org.gnome.evince.Window&quot;</span><span class="hl opt">)</span>
        <span class="hl kwa">del</span> self<span class="hl opt">.</span>_tmp_syncview
        self<span class="hl opt">.</span>_handler <span class="hl opt">=</span> <span class="hl kwa">None</span>
        <span class="hl kwa">return True</span>

<span class="hl slc">## This file can be used as a script to support forward search and backward search in vim.</span>
<span class="hl slc">## It should be easy to adapt to other editors. </span>
<span class="hl slc">##  evince_dbus  pdf_file  line_source input_file</span>
<span class="hl kwa">if</span> __name__ <span class="hl opt">==</span> <span class="hl str">'__main__'</span><span class="hl opt">:</span>
    <span class="hl kwa">import</span> dbus<span class="hl opt">.</span>mainloop<span class="hl opt">.</span>glib<span class="hl opt">,</span> sys<span class="hl opt">,</span> os<span class="hl opt">,</span> logging
    <span class="hl kwa">from</span> gi<span class="hl opt">.</span>repository <span class="hl kwa">import</span> GObject

    <span class="hl kwa">def</span> <span class="hl kwd">print_usage</span><span class="hl opt">():</span>
        <span class="hl kwa">print</span><span class="hl opt">(</span><span class="hl str">'''</span>
<span class="hl str">The usage is evince_dbus output_file line_number input_file from the directory of output_file.</span>
<span class="hl str">'''</span><span class="hl opt">)</span>
        sys<span class="hl opt">.</span><span class="hl kwd">exit</span><span class="hl opt">(</span><span class="hl num">1</span><span class="hl opt">)</span>

    <span class="hl kwa">if</span> <span class="hl kwb">len</span><span class="hl opt">(</span>sys<span class="hl opt">.</span>argv<span class="hl opt">)!=</span><span class="hl num">4</span><span class="hl opt">:</span>
        <span class="hl kwd">print_usage</span><span class="hl opt">()</span>
    <span class="hl kwa">try</span><span class="hl opt">:</span>
        line_number <span class="hl opt">=</span> <span class="hl kwb">int</span><span class="hl opt">(</span>sys<span class="hl opt">.</span>argv<span class="hl opt">[</span><span class="hl num">2</span><span class="hl opt">])</span>
    <span class="hl kwa">except</span> <span class="hl kwc">ValueError</span><span class="hl opt">:</span>
        <span class="hl kwd">print_usage</span><span class="hl opt">()</span>

    output_file <span class="hl opt">=</span> sys<span class="hl opt">.</span>argv<span class="hl opt">[</span><span class="hl num">1</span><span class="hl opt">]</span>
    input_file  <span class="hl opt">=</span> sys<span class="hl opt">.</span>argv<span class="hl opt">[</span><span class="hl num">3</span><span class="hl opt">]</span>
    path_output  <span class="hl opt">=</span> os<span class="hl opt">.</span><span class="hl kwd">getcwd</span><span class="hl opt">() +</span> <span class="hl str">'/'</span> <span class="hl opt">+</span> output_file
    path_input   <span class="hl opt">=</span> os<span class="hl opt">.</span><span class="hl kwd">getcwd</span><span class="hl opt">() +</span> <span class="hl str">'/'</span> <span class="hl opt">+</span> input_file

    <span class="hl kwa">if not</span> os<span class="hl opt">.</span>path<span class="hl opt">.</span><span class="hl kwd">isfile</span><span class="hl opt">(</span>path_output<span class="hl opt">):</span>
        <span class="hl kwd">print_usage</span><span class="hl opt">()</span>

    dbus<span class="hl opt">.</span>mainloop<span class="hl opt">.</span>glib<span class="hl opt">.</span><span class="hl kwd">DBusGMainLoop</span><span class="hl opt">(</span>set_as_default<span class="hl opt">=</span><span class="hl kwa">True</span><span class="hl opt">)</span>
    logger <span class="hl opt">=</span> logging<span class="hl opt">.</span><span class="hl kwd">getLogger</span><span class="hl opt">(</span><span class="hl str">&quot;evince_dbus&quot;</span><span class="hl opt">)</span>
    logger<span class="hl opt">.</span><span class="hl kwd">setLevel</span><span class="hl opt">(</span>logging<span class="hl opt">.</span>DEBUG<span class="hl opt">)</span>
    ch <span class="hl opt">=</span> logging<span class="hl opt">.</span><span class="hl kwd">StreamHandler</span><span class="hl opt">()</span>
    ch<span class="hl opt">.</span><span class="hl kwd">setLevel</span><span class="hl opt">(</span>logging<span class="hl opt">.</span>DEBUG<span class="hl opt">)</span>

    formatter <span class="hl opt">=</span> logging<span class="hl opt">.</span><span class="hl kwd">Formatter</span><span class="hl opt">(</span><span class="hl str">'%(asctime)s - %(name)s - %(levelname)s - %(message)s'</span><span class="hl opt">)</span>

    ch<span class="hl opt">.</span><span class="hl kwd">setFormatter</span><span class="hl opt">(</span>formatter<span class="hl opt">)</span>

    logger<span class="hl opt">.</span><span class="hl kwd">addHandler</span><span class="hl opt">(</span>ch<span class="hl opt">)</span>    
    a <span class="hl opt">=</span> <span class="hl kwd">EvinceWindowProxy</span><span class="hl opt">(</span><span class="hl str">'file://'</span> <span class="hl opt">+</span> path_output<span class="hl opt">,</span> <span class="hl kwa">True</span><span class="hl opt">,</span>logger<span class="hl opt">=</span>logger<span class="hl opt">)</span>
    
    <span class="hl kwa">def</span> <span class="hl kwd">sync_view</span><span class="hl opt">(</span>ev_window<span class="hl opt">,</span> path_input<span class="hl opt">,</span> line_number<span class="hl opt">):</span>
        ev_window<span class="hl opt">.</span><span class="hl kwd">SyncView</span> <span class="hl opt">(</span>path_input<span class="hl opt">, (</span>line_number<span class="hl opt">,</span> <span class="hl num">1</span><span class="hl opt">),</span><span class="hl num">0</span><span class="hl opt">)</span>

    GObject<span class="hl opt">.</span><span class="hl kwd">timeout_add</span><span class="hl opt">(</span><span class="hl num">400</span><span class="hl opt">,</span> sync_view<span class="hl opt">,</span> a<span class="hl opt">,</span> path_input<span class="hl opt">,</span> line_number<span class="hl opt">)</span>
    loop <span class="hl opt">=</span> GObject<span class="hl opt">.</span><span class="hl kwd">MainLoop</span><span class="hl opt">()</span>
    loop<span class="hl opt">.</span><span class="hl kwd">run</span><span class="hl opt">()</span> 
<span class="hl slc"># ex:ts=4:et:</span>
</code></pre></td></tr></table>
</div> <!-- class=content -->
</div>
  <div id="footer_community"></div>

  <div id="footer_grass"></div>

  <div id="footer">
    <div class="container_13" id="container_12">
      <div class="links grid_9">
        <div class="menu-footer-container">
          <ul id="menu-footer" class="menu">
            <li id="menu-item-1048" class=
            "menu-item menu-item-type-custom menu-item-object-custom current-menu-item current_page_item menu-item-1048">
            <a href="/">The GNOME Project</a>

              <ul class="sub-menu">
                <li id="menu-item-1049" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-1049">
                <a href="https://www.gnome.org/about/">About Us</a></li>

                <li id="menu-item-1050" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-1050">
                <a href="https://www.gnome.org/get-involved/">Get Involved</a></li>

                <li id="menu-item-1051" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-1051">
                <a href="https://www.gnome.org/teams/">Teams</a></li>

                <li id="menu-item-1053" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-1053">
                <a href="https://www.gnome.org/support-gnome/">Support GNOME</a></li>

                <li id="menu-item-1054" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-1054">
                <a href="https://www.gnome.org/contact/">Contact Us</a></li>

                <li id="menu-item-2246" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-2246">
                <a href="https://www.gnome.org/foundation/">The GNOME Foundation</a></li>
              </ul>
            </li>

            <li id="menu-item-1047" class=
            "menu-item menu-item-type-custom menu-item-object-custom menu-item-1047">
              <a href="#">Resources</a>

              <ul class="sub-menu">
                <li id="menu-item-1055" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1055">
                <a href="https://developer.gnome.org">Developer Center</a></li>

                <li id="menu-item-1056" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1056">
                <a href="https://help.gnome.org">Documentation</a></li>

                <li id="menu-item-1057" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1057">
                <a href="https://wiki.gnome.org">Wiki</a></li>

                <li id="menu-item-1058" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1058">
                <a href="https://mail.gnome.org/mailman/listinfo">Mailing Lists</a></li>

                <li id="menu-item-1059" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1059">
                <a href="https://wiki.gnome.org/GnomeIrcChannels">IRC Channels</a></li>

                <li id="menu-item-1060" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1060">
                <a href="https://bugzilla.gnome.org/">Bug Tracker</a></li>

                <li id="menu-item-1061" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1061">
                <a href="https://git.gnome.org/browse/">Development Code</a></li>

                <li id="menu-item-1062" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1062">
                <a href="https://wiki.gnome.org/Jhbuild">Build Tool</a></li>
              </ul>
            </li>

            <li id="menu-item-1046" class=
            "menu-item menu-item-type-custom menu-item-object-custom menu-item-1046">
              <a href="/news">News</a>

              <ul class="sub-menu">
                <li id="menu-item-1063" class=
                "menu-item menu-item-type-post_type menu-item-object-page menu-item-1063">
                <a href="https://www.gnome.org/press/">Press Releases</a></li>

                <li id="menu-item-1064" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1064">
                <a href="https://www.gnome.org/start/stable">Latest Release</a></li>

                <li id="menu-item-1065" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1065">
                <a href="https://planet.gnome.org">Planet GNOME</a></li>

                <li id="menu-item-1067" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1067">
                <a href="https://news.gnome.org">Development News</a></li>

                <li id="menu-item-1068" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1068">
                <a href="https://identi.ca/gnome">Identi.ca</a></li>

                <li id="menu-item-1069" class=
                "menu-item menu-item-type-custom menu-item-object-custom menu-item-1069">
                <a href="https://twitter.com/gnome">Twitter</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>

      <div id="footnotes" class="grid_9">
<p>Copyright &copy; 2004&ndash;2014, <a href="https://www.gnome.org/">The GNOME Project</a>.</p>
<br />
  <small><p>Hosted by <a href="http://www.redhat.com/">Red Hat</a>. 
   Powered by <a href="http://hjemli.net/git/cgit/">cgit</a>.</p>
  <p>To follow the commits, subscribe to <a href="http://mail.gnome.org/mailman/listinfo/commits-list">commits-list</a>. (can be limited to specific modules)</p></small>
</div>
    </div>
  </div>
</div> <!-- id=cgit -->
</body>
</html>
