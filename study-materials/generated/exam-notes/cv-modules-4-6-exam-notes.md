# CV Modules 4-6 — Exam Notes
**Subject:** Computer Vision
**Coverage:** Module 4, Module 5, Module 6
**Source files:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx), [subjects/CV/M4/jsd and kl CV m4.pdf](subjects/CV/M4/jsd%20and%20kl%20CV%20m4.pdf), [subjects/CV/M4/min max CV gan loss m4.pdf](subjects/CV/M4/min%20max%20CV%20gan%20loss%20m4.pdf), [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx), [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx)
**Generated:** 2026-05-02

## Coverage Note
- The PPTX decks were extracted slide-by-slide from their text layers.
- The two Module 4 PDFs were OCR-checked page by page; the OCR was noisy, so the notes below keep to the legible content that could be recovered reliably.
- Diagram-heavy slides are described in context even when the rendered image text was not fully machine-readable.

---

## 4. Generative Adversarial Networks (GANs)

### 4.1 Core idea
**Definition:** A GAN is a generative model with two neural networks: a generator and a discriminator.
- The **generator** creates fake samples from random noise.
- The **discriminator** tries to tell real samples from fake samples.
- Training is adversarial: each network improves by competing against the other.

**Why the fake data can look real:** The generator keeps learning from the discriminator's feedback until it produces outputs that are hard to distinguish from real data.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 5, 8, 18-19, 22-29.

> Figure: The slide deck uses a real-vs-fake face example, then maps the idea to GANs as a two-player game.

### 4.2 Origin and motivation
- Ian Goodfellow is credited as the father of GANs.
- The concept was introduced in the 2014 paper *Generative Adversarial Networks*.
- The slides connect GANs to creative AI outputs such as generated portraits, faces in games, synthetic art, music, and video.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 9-15.

### 4.3 GAN workflow
1. Sample random noise from a latent space.
2. Feed the noise into the generator.
3. Produce synthetic data.
4. The discriminator classifies inputs as real or fake.
5. Both networks are trained together in an adversarial loop.

**Key point:** The noise vector is important because it gives the generator a flexible starting point for producing diverse outputs.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 18-19, 29-34.

### 4.4 GAN architecture
- The architecture starts with a noise vector drawn from a simple distribution.
- The generator maps that latent input into a data sample.
- The discriminator gets both real data and generated data.
- Feedback from discriminator loss is sent back through backpropagation.

> Figure: The architecture slide shows the generator and discriminator as a feedback loop, with the generator improving from discriminator loss.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 22-29.

### 4.5 Why use a noise vector
- It injects randomness so the generator does not produce the same sample every time.
- It lets the model explore a large latent space.
- It supports diversity in generated data.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 30-34.

### 4.6 Implicit vs explicit density
- GANs are presented as **implicit density** models.
- Implicit density means the model learns to generate realistic samples without explicitly computing the data probability distribution.
- The slides contrast this with **explicit density** models such as VAEs.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 35-37.

### 4.7 Limitations of vanilla GANs
**Main issues listed in the slides:**
- Mode collapse: the generator keeps producing very similar outputs.
- Training instability.
- Vanishing gradients.
- Difficult hyperparameter tuning.
- No explicit probability distribution.

**Meaning of mode collapse:** even if the training data is diverse, the generator may keep repeating the same few outputs.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 38-46.

### 4.8 GAN variants

#### Conditional GAN (CGAN)
- Generation is conditioned on labels.
- This gives control over the output class.
- The objective changes because labels are added to the GAN setup.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 48-49, 57.

#### DCGAN
- Uses convolutional layers instead of only fully connected layers.
- The generator progressively upsamples from low spatial size to full image size.
- The discriminator uses convolution and downsampling.
- The slide lists a typical flow such as 4x4 -> 8x8 -> 16x16 -> 32x32 -> 64x64.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 50-51.

> Figure: The DCGAN architecture slide shows a generator that upsamples noise into an RGB image and a discriminator that compresses images back to a real/fake decision.

#### Progressive GAN
- Mentioned as an advanced GAN variant.

#### WGAN
- Uses Wasserstein distance instead of the basic GAN loss.
- The slides emphasize that the gradient remains meaningful and avoids saturation issues seen in the original loss.

#### StyleGAN
- Another advanced GAN variant mentioned in the deck.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 46-47, 52-54, 56.

### 4.9 Min-max objective and losses
The slide and OCR material indicate the standard GAN objective:

$$
\min_G \max_D V(D,G) = \mathbb{E}_{x \sim p_{data}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
$$

**Interpretation:**
- The discriminator tries to maximize correct classification of real and fake data.
- The generator tries to minimize the discriminator's ability to detect its outputs.

**Practical note from the slides:**
- The term $\log(1 - D(G(z)))$ can saturate, which leads to vanishing gradients.
- The WGAN idea is presented as a fix because it uses a more informative distance signal.

**Source:** [subjects/CV/M4/min max CV gan loss m4.pdf](subjects/CV/M4/min%20max%20CV%20gan%20loss%20m4.pdf), [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 55-57.

### 4.10 JSD and KL divergence
- The PDF titled with JSD/KL compares divergence measures between probability distributions.
- The slides use JSD as a way to measure similarity or difference between real and generated data distributions.
- KL divergence is also discussed in the PDF as part of the distribution-comparison context.

**Exam takeaway:** In GAN training, these divergences are used to describe how far the generated distribution is from the real distribution.

**Source:** [subjects/CV/M4/jsd and kl CV m4.pdf](subjects/CV/M4/jsd%20and%20kl%20CV%20m4.pdf), [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 58-61.

### 4.11 Evaluation metrics

#### Inception Score (IS)
- The slides describe IS as a measure of **quality + diversity**.
- High IS is good.
- It checks whether images are classifiable and whether the generated set spans multiple classes.
- It does not directly compare generated images to real images.

#### Frechet Inception Distance (FID)
- FID is described as a measure of realism.
- Low FID is good.
- It compares generated images against real images in feature space.
- It is more directly tied to similarity with the real data distribution.

#### Relation to mode collapse
- Mode collapse hurts diversity.
- IS can become misleading if generated images are classifiable but not diverse.
- FID becomes high when the generated distribution is too narrow or does not match the real distribution.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 62-69.

### 4.12 Applications
- Realistic face generation.
- Artificial portraits and creative art.
- Gaming avatars and synthetic faces.
- Healthcare image synthesis and medical imaging support.
- ViTs are mentioned as image-understanding models, while GANs are positioned as image-generation models.

**Source:** [subjects/CV/M4/CV Module 4 Mrudul.pptx](subjects/CV/M4/CV%20Module%204%20Mrudul.pptx) slides 11-17.

---

## 5. Object Segmentation and Related Vision Concepts

### 5.1 Segmentation basics
**Definition:** Segmentation divides an image into meaningful parts or sections.
- Image segmentation groups pixels with similar visual characteristics.
- The slides connect segmentation to clustering.
- Visual characteristics include properties such as line width, length, direction, focus, and other appearance cues.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 2-8.

### 5.2 Pixel and image basics
- An image of resolution 1024 x 768 contains 1,024 x 768 = 786,432 pixels.
- Pixel count does not by itself define physical size.
- DPI/PPI matters for print and screen quality.
- The slides state 300 DPI for high-quality print and 72/96 PPI for web images on screen.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 4-6.

### 5.3 Major segmentation types
- **Semantic segmentation:** all pixels of the same category are assigned one label.
- **Instance segmentation:** each object instance gets a separate label, even if the category is the same.
- **Panoptic segmentation:** combines semantic and instance segmentation.

**Things vs stuff in panoptic segmentation:**
- **Things** are countable objects such as cars, people, animals, furniture.
- **Stuff** refers to uncountable regions such as sky or road.
- The slides mention KITTI and autonomous-driving style datasets as examples.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 9-11.

> Figure: Panoptic segmentation is introduced as a blend of object-instance labeling and region labeling.

### 5.4 Segmentation vs object detection
- Segmentation classifies pixels.
- Object detection finds and labels objects using bounding boxes.
- Object localization identifies where the main subject is.
- The slides explicitly contrast semantic segmentation and object detection.
- Segmentation is preferred when fine boundary information matters.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 12-15.

### 5.5 Scene parsing and autonomous driving
- Scene parsing means labeling every region and understanding relationships such as car on road or person near building.
- Autonomous driving is a main application because segmentation helps identify roads, people, vehicles, and obstacles.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 15-16.

### 5.6 Motion-related segmentation ideas
- The slides note that in videos, optical flow tracks pixel movement, while semantic flow tracks the same semantic entity across frames.
- This sits at the boundary between segmentation and video understanding.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slide 17.

### 5.7 Bilinear interpolation
- Bilinear interpolation estimates a pixel value at a new location using the four nearest neighbors.
- It is used during image resizing and resampling.
- If a new point lies exactly at the center of four neighbors, the weights become equal and the result reduces to averaging.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 19-24.

### 5.8 Symmetry in segmentation
- Symmetry is not itself a segmentation method.
- It is a useful prior or constraint.
- In medical imaging, especially brain MRI, symmetry helps detect asymmetry such as tumors.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 29-30.

### 5.9 Image pyramids and receptive field
- An image pyramid is a sequence of downscaled versions of the same image.
- It helps detect objects at multiple scales.
- Downscaling gives different zoom levels and helps models capture both fine and coarse structure.
- Receptive field is the area of the input image that a neuron depends on.
- Deeper layers have a larger receptive field and capture larger context.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 31-35.

### 5.10 Pixel-wise softmax
- Pixel-wise softmax applies softmax independently at each pixel location.
- It turns class scores into per-pixel class probabilities that sum to 1.
- This is a standard step in semantic segmentation.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 36-37.

### 5.11 PSPNet
**Meaning:** PSPNet stands for Pyramid Scene Parsing Network.
- It is designed for semantic segmentation.
- Pyramid pooling extracts features at multiple spatial scales.
- The pooled features are concatenated to combine local and global context.
- Final prediction is done with pixel-wise softmax.

> Figure: The PSPNet slides show pyramid pooling over multiple regions, concatenation of multi-scale features, and final per-pixel classification.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 38-42.

### 5.12 FPN
**Meaning:** Feature Pyramid Network uses a single CNN backbone to produce a pyramid of feature maps.
- Bottom-up pathway: a normal CNN creates feature maps such as C2, C3, C4, C5.
- Top-down pathway: high-level semantic information is upsampled.
- Lateral connections merge top-down semantics with bottom-up spatial detail.
- FPN avoids the cost of repeatedly resizing the input image.

> Figure: The FPN slides show bottom-up feature extraction, top-down upsampling, and lateral merges.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 44-51.

### 5.13 U-Net
- U-Net is a U-shaped segmentation architecture.
- The contracting path acts as an encoder and reduces spatial size while increasing feature depth.
- The expansive path acts as a decoder and restores resolution.
- Skip connections preserve fine details and boundaries that would otherwise be lost.
- The slides mention filter counts like 64, 128, 256 and the bottleneck at the center of the U.
- The output is a segmented image where each pixel is classified.

**Application mentioned:** tumor detection in MRI scans.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 53-59.

### 5.14 Clustering-based segmentation
- Pixels can be grouped using similarity-based clustering.
- Algorithms mentioned: K-means, hierarchical clustering, DBSCAN, and mean shift.
- K-means groups pixels by minimizing within-cluster variance.
- Mean shift finds dense regions without predefining the number of clusters.
- DBSCAN groups dense points and labels isolated points as noise.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 63-65.

### 5.15 Hierarchical clustering and linkage
Linkage types listed in the deck:
- Single linkage: shortest distance between clusters.
- Complete linkage: longest distance between clusters.
- Average linkage: average pairwise distance.
- Centroid linkage: distance between cluster centroids.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slide 66.

### 5.16 Distance metrics
The slides list several metrics and when to choose them.
- Euclidean distance: straight-line distance.
- Cosine similarity: angle-based similarity.
- Hamming distance: number of differing positions in equal-length strings.
- Minkowski distance: general family that includes Euclidean and Manhattan.
- Chebyshev distance: maximum coordinate difference.
- Jaccard index: set overlap ratio.

**Selection rule:** choose based on the data type, sparsity/density, and whether similarity or distance is more important.

**Source:** [subjects/CV/M5/CV Module 5 Mrudul .pptx](subjects/CV/M5/CV%20Module%205%20Mrudul%20.%20pptx) slides 68-72.

---

## 6. Action Recognition, Tracking, Motion, and 3D Vision

### 6.1 Why video understanding is needed
- A single image is spatial; it does not capture time.
- Actions are temporal, so video is required.
- The slide example shows that a person with arms stretched can be ambiguous in one frame, but the full video makes the action clear.
- Video understanding is about extracting meaning from a sequence of frames.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 4-12.

### 6.2 Recognition vs tracking
- **Action recognition:** what is happening.
- **Object tracking:** where the object is over time.
- The slides explicitly say: recognition tells what, tracking tells where.

**Applications mentioned:** surveillance, self-driving cars, healthcare monitoring, robotics, autonomous systems.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 6-10.

### 6.3 Video basics
- A video is a sequence of frames displayed over time.
- Key components: frames, frame rate (fps), and time.
- The notation is image = $(x, y)$ and video = $(x, y, t)$.
- Typical frame-rate examples: 24 fps for movies, 30 fps for normal video, 60 fps for smooth motion.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 12-16.

### 6.4 Spatio-temporal features
- Spatial features describe appearance: shape, color, object identity.
- Temporal features describe motion and change across frames.
- Both are needed to distinguish actions such as walking vs running.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slide 17.

### 6.5 Action recognition
- Action recognition identifies the activity in a video sequence.
- Input is a sequence of frames.
- Classical approaches used handcrafted motion vectors.
- Deep learning approaches include CNNs, 3D CNNs, RNNs, and Transformers.
- The slides emphasize that modern methods learn spatio-temporal features automatically.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slide 13.

### 6.6 Object tracking
- Object tracking continuously locates an object across frames.
- The pipeline shown in the slides:
  - initialization by detecting the object in the first frame,
  - motion estimation,
  - appearance modeling,
  - association across frames,
  - update.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slide 14.

### 6.7 Motion analysis
- Motion analysis is the systematic measurement and evaluation of movement.
- It is used to detect movement, track objects, and understand actions.
- The slides separate the process into capture, analysis, and interpretation.
- Analysis can use kinematics, dynamics, signal processing, and machine learning.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 25-31.

### 6.8 Kinematics and dynamics
- **Kinematics** studies motion without forces: position, velocity, acceleration.
- **Dynamics** studies the forces and torques causing motion.
- The slides connect dynamics to Newton's second law and Euler's rotation equations.
- In computer vision, the practical focus is usually on estimating motion from images rather than directly measuring forces.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 33-46.

### 6.9 Methods of capture
- Marker-based systems use reflective markers on body points.
- Markerless systems use cameras and AI to detect key points directly.
- The slides connect markerless systems to pose estimation.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 36-38.

### 6.10 Motion models
The slides classify motion models as:
- Point mass model: object treated as a single moving point.
- Rigid body model: object moves as one solid piece.
- Articulated body model: multiple rigid parts connected by joints.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 40-44.

### 6.11 Optical flow
- Optical flow estimates how pixels move from one frame to the next.
- It represents apparent motion using arrows with direction and speed.
- The brightness constancy assumption says the intensity of a moving pixel remains constant over time.
- The slide formulation relates spatial and temporal intensity change to motion components $u$ and $v$.
- The aperture problem appears because one local equation cannot uniquely determine both motion components.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 47-53.

> Figure: The optical-flow slides show arrows between consecutive frames and explain that the measured motion is apparent motion of intensity patterns.

### 6.12 Lucas-Kanade method
- Uses local motion consistency: nearby pixels in a small window move similarly.
- The method forms multiple equations from a window and solves for $u$ and $v$.
- It is generally used for important points such as corners or features rather than every pixel.
- Interpretation from the slides:
  - $u > 0, v = 0$ -> motion right
  - $u < 0, v = 0$ -> motion left
  - $u = 0, v > 0$ -> motion down
  - $u = 0, v < 0$ -> motion up

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 54-59.

### 6.13 Horn-Schunck method
- Uses the same optical-flow equation as Lucas-Kanade.
- Assumes motion is smooth across the whole image.
- Solves for dense motion, meaning every pixel gets a motion vector.
- The slides emphasize regularization through smoothness across neighboring pixels.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 60-64.

### 6.14 Dense vs sparse flow
- Dense flow estimates motion for every pixel.
- Sparse flow estimates motion only at selected points.
- Lucas-Kanade is presented in a sparse-point setting.
- Horn-Schunck is presented in a dense-flow setting.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 54-64.

### 6.15 Motion-model based tracking
- Optical flow can be used for tracking objects across frames.
- The slides also mention Kalman filter and particle filter.
- Kalman filter is described as a simple and fast prediction-correction method.
- Particle filter is used when motion is more complex.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slide 66.

### 6.16 3D vision and stereo depth
- 3D vision estimates object depth from images.
- Humans use two eyes; computers use two cameras.
- Stereo vision uses two views taken from slightly different viewpoints.
- Stereo matching finds the corresponding point in left and right images.
- Disparity is the position difference of the same point in the two views.
- Depth is inversely proportional to disparity: closer objects have larger disparity, farther objects have smaller disparity.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slides 67-71.

### 6.17 Application example
- The slides mention Google Street View as an example connected to stereo vision and depth estimation.

**Source:** [subjects/CV/M6/CV_Module 6_Mrudul.pptx](subjects/CV/M6/CV_Module%206_Mrudul.pptx) slide 72.

---

## Quick Recall List
- GANs: generator vs discriminator, noise vector, adversarial training, mode collapse, CGAN, DCGAN, WGAN, StyleGAN, IS, FID.
- Segmentation: semantic, instance, panoptic, PSPNet, FPN, U-Net, clustering, distance metrics.
- Video: action recognition, tracking, motion analysis, optical flow, Lucas-Kanade, Horn-Schunck, stereo depth.

---

## Missing Coverage
- No additional syllabus file was provided, so the notes are organized by module folder rather than by a separate syllabus document.
- The two scanned Module 4 PDFs were partially garbled under OCR; the clearly legible GAN objective and divergence ideas were retained, but I did not force uncertain transcriptions into the notes.
