---
layout: post
categories: data
title: "AOS frame simulation data"
author: "鑫宇, 甲森"
date: 2023-02-13
tags: ['simulated experimental frames', ' synchronization codes', ' frame error control', ' CRC checksum', ' simulated experimental engineering parameter source packet', ' GPU frame parsing', ' source packet parsing performance']
---

The simulated experimental frames are 898 bytes long, the first 4 bytes are synchronization codes, the frame error control field is 2 bytes, and CRC checksum is used. The simulated experimental engineering parameter source packet is 390 bytes long, containing 467 parameters. It is used to test the GPU frame parsing and source packet parsing performance.

模拟实验帧长度为898字节，前4字节为同步码，帧差错控制域为2字节，采用CRC校验。模拟实验工程参数源包长度为390字节，包含467个参数，用于测试GPU帧解析和源包解析性能。

资源链接: [AOS frame simulation data](https://doi.org/10.57760/sciencedb.o00009.00474)
