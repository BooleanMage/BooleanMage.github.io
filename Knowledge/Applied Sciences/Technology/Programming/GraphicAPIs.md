---
layout: default
---

# DirectX11, 12, OpenGL, Vulkan

---
tags:
  - [[Programming]]
  - [[DirectX]]
  - [[OpenGL]]
  - [[Graphics]]
---

## Debug method
* GL: orbuculum
* DX: Enable Debug flag when create instance
* VK: Load Debug Layer

## Design 
* Async
  * dx11, 12: fence
  * gl, dx9: none
  * vk: sync primitive
* exectute sequence
  * gl, dx9: by cpu
  * dx11, dx12: fence
  * dx12, vk: barrier 


## Abstraction Level
* Application level
  * dx11: adapter
  * dx12: adapter, device
  * gl: state machine on instance
* Thread level
  * dx11: state machine on device
  * dx12: state machine on commandlist
  * gl, dx9: no
* Task level
  * dx11, gl: no
  * dx12: command allocator, command bundle
  * vk: command buffer


## GPU resource 
* Essential thing in DX
  * cpu, gpu r/w are incompatible
* Shader types
  * DX constant buffer(b1, b0 constant buffer views (CBV))  = GL/Vk uniform buffer 
  * DX structured buffer(u0, u1 unordered access views (UAV)) = GL/Vk shader storage Buffer
  * DX Texture (t0, t1 shader resource views (SRV)) = GL/Vk texture
* GPU resource
  * dx11: SRV, RTV......
  * dx12: Heap
