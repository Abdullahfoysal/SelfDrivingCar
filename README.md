## Working Repository: https://github.com/Abdullahfoysal/robotic-car

<h1>Lane Detection Implementation - Step 1</h1>
<p>Behavioral cloning for autonomous cars involves training a machine learning model to mimic the behavior of a human driver, using data collected from that driver's real-world driving experiences.</p>
<h2>🚀 Hardware Setup</h2>

<h3>🔧 Components Used</h3>
<ul>
  <li>Raspberry Pi</li>
  <li>Pi Camera</li>
  <li>Motor Controller (L298N Dual H Bridge)</li>
  <li>Power Controller (9V Battery or equivalent)</li>
</ul>

<h3>⚠️ Most Challenging Parts</h3>
<ul>
  <li>Managing hardware parts and Raspberry Pi GPIO initialization</li>
  <li>Motor controller connection and configuration</li>
  <li>Setting up and accessing the Pi Camera</li>
  <li>Load ML model </li>
</ul>

<h3>📷 Circuit Diagram</h3>
<p>The following diagram shows the complete connection between Raspberry Pi, motor controller, power supply, and camera:</p>
<p align="center">
<img src="project-demo-images/image2.png" alt="Lane Detection Hardware Setup" width="400" />
</p>

<h3>🧠 ML Model Overview</h3>
<p>The ML model used here is a convolutional neural network (CNN) that takes image frames as input, extracts features, and predicts lane positions. It includes:</p>
<ul>
  <li>Input Image (320 x 240 px)</li>
  <li>Convolutional Layers with ReLU and Max Pooling</li>
  <li>Fully Connected Network for final prediction</li>
</ul>

<h3>📌 Notes</h3>
<ul>
  <li>Ensure your Pi Camera is enabled via <code>raspi-config</code></li>
  <li>Use proper heat sinks for Raspberry Pi if running continuously</li>
  <li>Test GPIO pin logic before connecting to the motor controller</li>
</ul>

<hr>

<p>📁 For next steps, refer to <strong>Step 2: Lane Detection using Camera Feed</strong></p>

