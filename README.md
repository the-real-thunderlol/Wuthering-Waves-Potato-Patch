# WUTHERING WAVES POTATO PATCH

<img width="752" height="840" alt="image" src="https://github.com/user-attachments/assets/97142f14-1464-4405-a236-879f05e43b6f" />

Wuthering waves uses Unreal Engine.
Unreal Engine creates alot of settings files. And you can safetly modify them (does not change how the game works internally)
The following are the files I've defined in the Potato, Low, Medium settings. 

Config Folder: `Wuthering Waves Game\Client\Saved\Config\WindowsNoEditor`

Files:
- Engine.ini
- GameUserSettings.ini
- Scalability.ini
- DeviceProfiles.ini

These files will be copied into you Wuthering waves config folder after you select a choice. 
using Default or deleting all the Settings files from that folder will restore original settings.

# INTRESTING NOTE:
Game internal settings from menu dont affect Unreal Engine's External settings. You can mix and match them both.

# ==========

# EXAMPLE

I used a very weak card as an example to showcase how far it can go

CPU: 7950x3D
GPU: Quadro P1000 (weaker than a GTX 1050 BTW)
Screen: 1080p @ 60 Hz

#NORMAL (~35 FPS)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b6461d92-cd36-47a1-8c37-b23b4d7329c2" />
<img width="1165" height="913" alt="image" src="https://github.com/user-attachments/assets/620d01b9-8a2c-4511-8a17-034eed03f129" />


# POTATO (~45 FPS)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4c7c1511-5412-4cac-a75b-b9b3312a6492" />
<img width="1135" height="807" alt="image" src="https://github.com/user-attachments/assets/52f8ac89-ac23-4671-a202-3b077d7f046f" />


## RESULTS:
- 23% FPS BOOST. 
- Slightly less VRAM Intensive (2.7 GB vs 3 GB), will rush less towards SWAP Memory
- Overall a much more smoother experience.

===

# "HEY AI MAKE ME A TABLE OF WHAT I DID IM TOO LAZY TO... 😴"
# SETTINGS CHANGED:

| Setting | Default | Potato | Low | Medium |
|---|---|---|---|---|
| VRAM target | Game default | ~2 GB | ~3 GB | ~4 GB |
| GPU workload target | Baseline | ~25% | ~33% | ~50% |
| Resolution scale | 100% | 100% | 100% | 100% |
| View distance quality | 3 | 0 | 1 | 2 |
| Anti-aliasing quality | 3 | 1 | 1 | 2 |
| Shadow quality group | 3 | 0 | 0 | 1 |
| Post-processing quality | 3 | 0 | 0 | 1 |
| Texture quality | 4 | 0 | 1 | 2 |
| Effects quality | 3 | 0 | 1 | 2 |
| Foliage quality | 3 | 0 | 1 | 2 |
| Shading quality | 3 | 0 | 1 | 2 |
| Texture streaming pool | Inherited | 512 MB | 1,024 MB | 1,536 MB |
| Adaptive streaming mip bias | Inherited | 2 | 1 | 0 |
| Anisotropic filtering | Inherited | 1× | 2× | 4× |
| Environment texture limit | Inherited | 256px | 512px | 1,024px |
| Environment normal/specular limit | Inherited | 128px | 256px | 512px |
| Character/weapon texture limit | Inherited | 512px | 1,024px | 2,048px |
| Character/weapon normal/specular limit | Inherited | 256px | 512px | 1,024px |
| Effects texture limit | Inherited | 256px | 512px | 1,024px |
| Skybox texture limit | Inherited | 256px | 512px | 1,024px |
| View distance multiplier | Inherited | 0.40 | 0.60 | 0.80 |
| Static mesh LOD distance scale | Inherited | 2.50 | 1.75 | 1.25 |
| Skeletal mesh LOD bias | Inherited | +1 | +1 | 0 |
| Grass/foliage density scale | Inherited | 0.00 | 0.15 | 0.40 |
| Grass/foliage cull distance scale | Inherited | 0.40 | 0.60 | 0.80 |
| Dynamic shadows | Inherited | Disabled | Disabled | Reduced |
| Maximum dynamic shadow resolution | Inherited | Disabled | Disabled | 512px |
| Shadow cascades | Inherited | Disabled | Disabled | 1 |
| Ambient occlusion | Inherited | Disabled | Disabled | Low |
| Niagara effects quality | Inherited | 0 | 1 | 2 |
| Particle spawn multiplier | Inherited | 0.25 | 0.50 | 0.75 |
| Particle LOD bias | Inherited | +2 | +1 | 0 |
| Translucency lighting volume dimension | Inherited | 16 | 24 | 32 |
| Translucency volume blur | Inherited | Disabled | Disabled | Disabled |
| Detail mode | Inherited | 0 | 0 | 1 |
| Material quality | Inherited | Low | Low | Medium |
| Screen-space reflections | Inherited | Disabled | Disabled | Disabled |
| Refraction | Inherited | Disabled | Disabled | Disabled |
| Distance-field shadows | Inherited | Disabled | Disabled | Disabled |
| Volumetric fog | Inherited | Disabled | Disabled | Disabled |
| Light shafts/Tyndall scattering | Inherited | Disabled | Disabled | Disabled |
| Motion blur | Inherited | Disabled | Disabled | Disabled |
| Depth of field | Inherited | Disabled | Disabled | Disabled |
| Lens flare | Inherited | Disabled | Disabled | Disabled |
| Chromatic aberration | Inherited | Disabled | Disabled | Disabled |
| Bloom, including Kuro FFT bloom | Inherited | Disabled | Disabled | Disabled |
| Decorative vegetation/water interaction effects | Inherited | Disabled | Disabled | Disabled |

**Inherited:** unchanged settings supplied by the game.
**Targets:** VRAM and GPU workload figures are goals, not benchmark results.
