<div class="Box-sc-g0xbh4-0 bJMeLZ js-snippet-clipboard-copy-unpositioned" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div dir="auto">
<a href="https://sagemath.org" rel="nofollow">
  <themed-picture data-catalyst-inline="true" data-catalyst=""><picture>
    <source media="(prefers-color-scheme: dark)" srcset="/sagemath/sage/raw/develop/src/doc/common/static/logo_sagemath_white.svg">
    <img src="/sagemath/sage/raw/develop/src/doc/common/static/logo_sagemath_black.svg" height="60" align="left" style="visibility:visible;max-width:100%;">
  </picture></themed-picture>
</a>
   <em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">“创建 Magma、Maple、Mathematica 和 MATLAB 的可行开源替代方案”</font></font></em>
</div>
<h1 dir="auto"></h1>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 是根据 GNU 通用公共许可证 GPLv2+ 发布的开源数学软件，并包含具有</font></font><a href="/sagemath/sage/blob/develop/COPYING.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">兼容软件许可证</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">的软件包。
</font></font><a href="https://www.sagemath.org/development-map.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">全球各地的人们都</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为 Sage 的发展做出了贡献。</font></font><a href="https://doc.sagemath.org/html/en/index.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">完整文档</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可在线获取。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目录</font></font></h2><a id="user-content-table-of-contents" class="anchor" aria-label="固定链接：目录" href="#table-of-contents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><a href="#getting-started"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">入门</font></font></a></li>
<li><a href="#supported-platforms"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">支持的平台</font></font></a></li>
<li><a href="#windows-preparing-the-platform"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[Windows] 准备平台</font></font></a></li>
<li><a href="#macos-preparing-the-platform"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[macOS] 准备平台</font></font></a></li>
<li><a href="#instructions-to-build-from-source"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从源代码构建的说明</font></font></a></li>
<li><a href="#sagemath-docker-images"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">SageMath Docker 镜像</font></font></a></li>
<li><a href="#troubleshooting"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">故障排除</font></font></a></li>
<li><a href="#contributing-to-sage"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为圣人做出贡献</font></font></a></li>
<li><a href="#directory-layout"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目录布局</font></font></a></li>
<li><a href="#build-system"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建系统</font></font></a></li>
<li><a href="#relocation"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">搬迁</font></font></a></li>
<li><a href="#redistribution"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">再分配</font></font></a></li>
<li><a href="#build-system"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建系统</font></font></a></li>
<li><a href="#changes-to-included-software"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">附带软件的更改</font></font></a></li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">入门</font></font></h2><a id="user-content-getting-started" class="anchor" aria-label="永久链接：开始使用" href="#getting-started"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">那些不耐烦的人可以使用预构建的 Sage，可以从任何地方在线获取</font></font></p>
<p dir="auto"><a href="https://mybinder.org/v2/gh/sagemath/sage-binder-env/master" rel="nofollow"><img src="https://camo.githubusercontent.com/e91e1d353a8b6acf0b42547ac3901f2c30138a3abaaa3d3c242da30b5b4f8426/68747470733a2f2f6d7962696e6465722e6f72672f62616467655f6c6f676f2e737667" alt="活页夹" data-canonical-src="https://mybinder.org/badge_logo.svg" style="max-width: 100%;"></a> &nbsp; <a href="https://gitpod.io/#https://github.com/sagemath/sage/tree/master" rel="nofollow"><img src="https://camo.githubusercontent.com/ae79fbb17edaf2aa57ec8688b746de050226ac46d3c6c50a38c9cb3d2c64768c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476974706f642d52656164792d2d746f2d2d436f64652d626c75653f6c6f676f3d676974706f64" alt="Gitpod 准备编码" data-canonical-src="https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod" style="max-width: 100%;"></a> &nbsp; <a href="https://codespaces.new/sagemath/sage/tree/master" rel="nofollow"><img src="https://camo.githubusercontent.com/da721b6688ac8686053f807c9ed605072e43bb9c1e770f0031c192a5951aab14/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f70656e5f696e5f4769744875625f436f64657370616365732d626c61636b3f6c6f676f3d676974687562" alt="在 GitHub Codespaces 中打开" data-canonical-src="https://img.shields.io/badge/Open_in_GitHub_Codespaces-black?logo=github" style="max-width: 100%;"></a></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">无需本地安装。否则请继续阅读。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"></font><a href="https://doc.sagemath.org/html/en/installation/index.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 安装指南</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">提供</font><font style="vertical-align: inherit;">
了一个决策树，可指导您选择最适合您的安装类型。这包括从源代码构建、从包管理器获取 Sage、使用容器映像或在云中使用 Sage。</font></font></p>
<p dir="auto"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">本自述文件包含从源代码构建 Sage 的独立说明。</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
它假设您已经克隆了 git 存储库或
</font><font style="vertical-align: inherit;">以 tarball 的形式下载了</font></font><a href="https://www.sagemath.org/download-source.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">源代码。</font></font></a><font style="vertical-align: inherit;"></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您有疑问或遇到问题，请随时向</font></font><a href="https://groups.google.com/group/sage-support" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 支持邮件列表发送电子邮件或在</font></font></a><font style="vertical-align: inherit;"></font><a href="https://ask.sagemath.org" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ask Sage 问题与解答网站</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
上提问</font><font style="vertical-align: inherit;">。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">支持的平台</font></font></h2><a id="user-content-supported-platforms" class="anchor" aria-label="永久链接：支持的平台" href="#supported-platforms"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 尝试支持所有主要的 Linux 发行版、最新版本的 macOS 和 Windows（使用适用于 Linux 或虚拟化的 Windows 子系统）。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">有关特定 Sage 版本支持的平台的详细信息，请参阅</font><font style="vertical-align: inherit;">此版本</font><a href="https://wiki.sagemath.org/ReleaseTours" rel="nofollow"><font style="vertical-align: inherit;">发布之旅</font></a><font style="vertical-align: inherit;">的
</font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可用性和安装帮助部分。</font></font></em><font style="vertical-align: inherit;"></font><a href="https://wiki.sagemath.org/ReleaseTours" rel="nofollow"><font style="vertical-align: inherit;"></font></a><font style="vertical-align: inherit;"></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">我们高度赞赏对 Sage 的贡献，修复了可移植性错误并帮助将 Sage 移植到新平台；请通过</font></font><a href="https://groups.google.com/group/sage-devel" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sage-devel 邮件列表</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">告诉我们</font><font style="vertical-align: inherit;">。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[Windows] 准备平台</font></font></h2><a id="user-content-windows-preparing-the-platform" class="anchor" aria-label="永久链接：[Windows] 准备平台" href="#windows-preparing-the-platform"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">在 Windows 上运行 Sage 的首选方法是使用 Windows Subsystem for Linux (WSL)。按照
</font></font><a href="https://docs.microsoft.com/en-us/windows/wsl/faq" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">官方 WSL 安装指南</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
安装 Ubuntu（或其他 Linux 发行版）。确保为 WSL 分配足够的 RAM；已知 5GB 可以工作，而 2GB 可能不足以从源代码构建 Sage。然后适用于 Linux 中的所有安装说明。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">作为替代方案，您还可以使用 Docker（</font></font><a href="#sagemath-docker-images"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">见下文</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">）或其他虚拟化解决方案在 Windows 上运行 Linux。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[macOS] 准备平台</font></font></h2><a id="user-content-macos-preparing-the-platform" class="anchor" aria-label="永久链接：[macOS] 准备平台" href="#macos-preparing-the-platform"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您的 Mac 使用 Apple Silicon（M1、M2、M3；arm64）架构，并且您通过从旧版 Mac 传输文件来设置 Mac，请确保该目录</font></font><code>/usr/local</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">不包含 Homebrew（或其他软件）的旧副本您可能已复制的 x86_64 架构。请注意，M1 的 Homebrew 安装在</font></font><code>/opt/homebrew</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，而不是
</font></font><code>/usr/local</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您想使用 conda，请参阅</font><font style="vertical-align: inherit;">Sage 安装手册中</font></font><a href="https://doc.sagemath.org/html/en/installation/conda.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">有关 conda 的部分以获取指导。</font></font></a><font style="vertical-align: inherit;"></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">否则，我们强烈建议使用</font></font><a href="https://brew.sh/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">https://brew.sh/</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中的 Homebrew（“macOS 缺少的包管理器”） ，它提供了</font></font><code>gfortran</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
编译器和许多库。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">否则，如果您不想安装 Homebrew，则需要安装最新版本的 Xcode 命令行工具。打开终端窗口并运行</font></font><code>xcode-select --install</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">；然后在弹出的窗口中点击“安装”。如果 Xcode 命令行工具已安装，您可能需要输入 来检查是否需要更新</font></font><code>softwareupdate -l</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
</ul>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从源代码构建的说明</font></font></h2><a id="user-content-instructions-to-build-from-source" class="anchor" aria-label="永久链接：从源代码构建的说明" href="#instructions-to-build-from-source"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">与许多其他软件包一样，Sage 是使用
</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，然后是</font></font><code>make</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.但是，我们强烈建议您阅读以下构建 Sage 的分步说明。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">这些说明涵盖所有 Linux、macOS 和 WSL。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">提供这些说明背景的更多详细信息可以在</font></font><a href="https://doc.sagemath.org/html/en/installation/source.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">“从源代码安装”部分</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中找到。在安装指南中。</font></font></p>
<ol dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">确定源/构建目录 ( </font></font><code>SAGE_ROOT</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">)：</font></font></p>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">在个人计算机上，:envvar: 目录的任何子目录</font></font><code>HOME</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
都可以。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">例如，您可以使用</font></font><code>SAGE_ROOT=~/sage/sage</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，我们将使用它作为下面的运行示例。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">您需要至少 10 GB 的可用磁盘空间。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">源目录的完整路径不能包含</font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">空格</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">开始构建后，您无法在不破坏内容的情况下移动源/构建目录。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">您可能希望避免使用慢速文件系统，例如
</font></font><a href="https://en.wikipedia.org/wiki/Network_File_System" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">网络文件系统 (NFS)</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
等。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[macOS] macOS 允许在不使用精确大小写的情况下更改目录。针对 macOS 进行编译时请注意这种便利性。更改为 :envvar: 时忽略精确的大写</font></font><code>SAGE_ROOT</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可能会导致需要路径名中精确大写的依赖项出现构建错误。</font></font></p>
</li>
</ul>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用以下命令克隆源</font></font><code>git</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：</font></font></p>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">要检查其</font></font><code>git</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">是否可用，请打开终端并在 shell 提示符 ( </font></font><code>$</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) 下输入以下命令：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ git --version
  git version 2.42.0
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ git --version
  git version 2.42.0" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">确切的版本并不重要，但如果此命令出现错误，</font></font><code>git</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请使用包管理器进行安装，使用以下命令之一：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ sudo pacman -S git                          # on Arch Linux
  $ sudo apt-get update &amp;&amp; apt-get install git  # on Debian/Ubuntu
  $ sudo yum install git                        # on Fedora/Redhat/CentOS
  $ sudo zypper install git                     # on openSUSE
  $ sudo xbps-install git                       # on Void Linux
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ sudo pacman -S git                          # on Arch Linux
  $ sudo apt-get update &amp;&amp; apt-get install git  # on Debian/Ubuntu
  $ sudo yum install git                        # on Fedora/Redhat/CentOS
  $ sudo zypper install git                     # on openSUSE
  $ sudo xbps-install git                       # on Void Linux" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"></font><code>SAGE_ROOT</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">创建应建立的</font><font style="vertical-align: inherit;">目录：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ mkdir -p ~/sage
  $ cd ~/sage
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ mkdir -p ~/sage
  $ cd ~/sage" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">克隆 Sage git 存储库：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ git clone -c core.symlinks=true --filter blob:none  \
              --origin upstream --branch develop --tags \
              https://github.com/sagemath/sage.git
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ git clone -c core.symlinks=true --filter blob:none  \
              --origin upstream --branch develop --tags \
              https://github.com/sagemath/sage.git" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">此命令获取最新的开发版本。替换</font></font><code>--branch develop</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为</font></font><code>--branch master</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">选择最新的稳定版本。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">这将创建子目录</font></font><code>~/sage/sage</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。 （有关详细信息，请参阅《Sage 开发人员指南》中的</font></font><a href="https://doc.sagemath.org/html/en/developer/git_setup.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">“设置 git”</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">部分
</font><font style="vertical-align: inherit;">
和以下部分。）</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">切换到创建的子目录：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ cd sage
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ cd sage" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[Windows] Sage 源代码树包含符号链接，如果使用 Windows 行结尾而不是 UNIX 行结尾，则构建将无法工作。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">因此建议（但不是必须）使用 WSL 版本的</font></font><code>git</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
</li>
</ul>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">安装系统包。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请参阅《Sage 安装手册》中有关</font></font><a href="https://doc.sagemath.org/html/en/installation/source.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从源代码安装的部分，</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">以获取可以安装的系统软件包的编译。完成后，跳至步骤 7（引导）。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">或者，遵循下面更细粒度的方法。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[Linux、WSL] 安装所需的最低构建先决条件：</font></font></p>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">编译器：</font></font><code>gcc</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><code>gfortran</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><code>g++</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（支持从 8.4.0 到 13.x 的 GCC 版本以及最新版本的 Clang (LLVM)）。</font><font style="vertical-align: inherit;">
有关合适编译器的讨论，</font><font style="vertical-align: inherit;">请参阅</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/gcc/SPKG.rst"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">build/pkgs/gcc/SPKG.rst</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和
</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/gfortran/SPKG.rst"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">build/pkgs/gfortran/SPKG.rst 。</font></font></a><font style="vertical-align: inherit;"></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建工具：GNU </font><font style="vertical-align: inherit;">、</font></font><code>make</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">GNU </font><font style="vertical-align: inherit;">、</font></font><code>m4</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（</font></font><code>perl</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">包括
</font></font><code>ExtUtils::MakeMaker</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">）</font></font><code>ranlib</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、、、、、</font><font style="vertical-align: inherit;">。</font><font style="vertical-align: inherit;">有关更多详细信息，</font><font style="vertical-align: inherit;">请参阅</font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/SPKG.rst"><font style="vertical-align: inherit;">build/pkgs/_prereq/SPKG.rst 。</font></a></font><code>git</code><font style="vertical-align: inherit;"></font><code>tar</code><font style="vertical-align: inherit;"></font><code>bc</code><font style="vertical-align: inherit;"></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/SPKG.rst"><font style="vertical-align: inherit;"></font></a><font style="vertical-align: inherit;"></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Python 3.4 或更高版本，或 Python 2.7，完整安装包括
</font></font><code>urllib</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">；但理想的版本是 3.9.x、3.10.x、3.11.x、3.12.x，这将避免构建 Sage 自己的 Python 3 副本。</font><font style="vertical-align: inherit;">
有关更多详细信息，请参阅</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/python3/SPKG.rst"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">build/pkgs/python3/SPKG.rst 。</font></font></a><font style="vertical-align: inherit;"></font></p>
</li>
</ul>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">我们收集了提供这些构建先决条件的系统包列表。请参阅文件夹
</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">build/pkgs/_prereq/distros</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中的文件
</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros/arch.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">arch.txt</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、
 </font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros/debian.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">debian.txt</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
（也适用于 Ubuntu、Linux Mint 等）、
 </font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros/fedora.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">fedora.txt</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
（也适用于 Red Hat、CentOS）、
 </font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros/opensuse.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">opensuse.txt</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、
 </font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros/slackware.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">slackware.txt</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和
</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_prereq/distros/void.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">void.txt</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，或访问
</font></font><a href="https://doc.sagemath.org/html/en/reference/spkg/_prereq.html#spkg-prereq" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">https://doc.sagemath.org/html/en/reference/spkg/_prereq.html#spkg-prereq</font></font></a></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：建议您安装 LaTeX 和 ImageMagick 工具（例如“转换”命令），因为某些绘图功能可以受益于它们。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[开发] 如果您计划进行 Sage 开发或以其他方式使用票据分支而不仅仅是发布，请安装引导先决条件。请参阅文件夹
</font></font><a href="/sagemath/sage/blob/develop/build/pkgs/_bootstrap/distros"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">build/pkgs/_bootstrap/distros</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中的文件，或访问
</font></font><a href="https://doc.sagemath.org/html/en/reference/spkg/_bootstrap.html#spkg-bootstrap" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">https://doc.sagemath.org/html/en/reference/spkg/_bootstrap.html#spkg-bootstrap</font></font></a></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用以下命令引导源树：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>$ make configure
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ make configure" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（如果未安装引导先决条件，此命令将下载提供预构建引导输出的包。）</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">清理构建环境。使用命令</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>$ env
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ env" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">检查当前环境变量，特别是</font></font><code>PATH</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、
 </font></font><code>PKG_CONFIG_PATH</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><code>LD_LIBRARY_PATH</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><code>CFLAGS</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><code>CPPFLAGS</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><code>CXXFLAGS</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和</font></font><code>LDFLAGS</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（如果设置）。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从这些（以冒号分隔的）环境变量中删除 Sage 不应将其用于其自己的构建的项目。特别是，如果项目引用了以前的 Sage 安装，请删除它们。</font></font></p>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[WSL] 特别是，WSL 将许多项目从 Windows
</font></font><code>PATH</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">变量导入到 Linux 环境中，这可能会导致令人困惑的构建错误。这些项目通常以 开头</font></font><code>/mnt/c</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。最好将它们从环境变量中全部删除。例如，您可以</font></font><code>PATH</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用以下命令进行设置：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ export PATH=/usr/sbin/:/sbin/:/bin/:/usr/lib/wsl/lib/
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ export PATH=/usr/sbin/:/sbin/:/bin/:/usr/lib/wsl/lib/" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[macOS with homebrew] 设置构建所需的环境变量：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>  $ source ./.homebrew-build-env
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="  $ source ./.homebrew-build-env" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">这是为了使一些 Homebrew 的软件包（所谓的 keg-only 软件包）可用于构建。运行一次以应用当前终端会话的建议。在从新的终端会话重建 Sage 之前或安装其他自制程序包之后，您可能需要重复此命令。 （您还可以将其添加到您的 shell 配置文件中，以便它在以后的所有会话中自动运行。）</font></font></p>
</li>
</ul>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（可选）决定安装前缀 ( </font></font><code>SAGE_LOCAL</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">)：</font></font></p>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">传统上，默认情况下，Sage 安装到根目录为 的子目录层次结构中</font></font><code>SAGE_ROOT/local/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可以使用 进行更改</font></font><code>./configure --prefix=SAGE_LOCAL</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，其中</font></font><code>SAGE_LOCAL</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">是所需的安装前缀，该前缀必须可由用户写入。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果将此选项与 结合使用</font></font><code>--disable-editable</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，则可以在完成构建过程后删除整个 Sage 源树。安装的</font></font><code>SAGE_LOCAL</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">将是 Sage 的独立安装。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请注意，在 Sage 的构建过程中，</font></font><code>make</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建</font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">并</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
安装（</font></font><code>make install</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">是无操作）。因此，安装层次结构必须可由用户写入。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您想安装到共享位置（例如</font></font><code>/usr/local/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.不要尝试将 Sage 构建为</font></font><code>root</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
</li>
</ul>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（可选）查看配置选项，其中包括许多可选包：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>$ ./configure --help
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ ./configure --help" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 开发人员值得注意的选项如下：</font></font></p>
<ul dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用该选项</font></font><code>--config-cache</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可以</font></font><code>configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
保留配置值的磁盘缓存。当尝试进行包升级的票证分支时，这会带来很好的加速，这涉及自动重新运行配置步骤。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用该选项</font></font><code>--enable-ccache</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">让 Sage 安装并使用可选包</font></font><code>ccache</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，该包预先配置为保留从源文件创建的对象文件的磁盘缓存。这可以在不同分支之间切换时提供极大的加速，但会占用磁盘空间。</font></font></p>
</li>
</ul>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选，但强烈推荐：设置一些环境变量来自定义构建。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">例如，</font></font><code>MAKE</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">环境变量控制是否并行运行多个作业。例如，在具有 4 个处理器的机器上，键入</font></font><code>export MAKE="make -j4"</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">将配置构建脚本以使用 4 个作业执行 Sage 的并行编译。在一些功能强大的机器上，您甚至可能会考虑</font></font><code>-j16</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，因为使用比 CPU 核心更多的作业进行构建可以进一步加快速度。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">要减少构建期间的终端输出，请输入</font></font><code>export V=0</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。 （</font></font><code>V</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">代表“冗长”。）</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">一些环境变量值得特别提及：</font></font><code>CC</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、
</font></font><code>CXX</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和</font></font><code>FC</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。这些定义编译器的变量可以在配置时设置，并且它们的值将被记录下来以供在构建时和运行时进一步使用。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">有关构建 Sage 的更多环境变量的深入讨论，请参阅</font></font><a href="https://doc.sagemath.org/html/en/installation/source.html#environment-variables" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">安装指南</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">键入</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，然后键入您要使用的任何选项。例如，要</font></font><code>gf2x</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用 Sage 提供的包构建 Sage，请使用</font></font><code>./configure --with-system-gf2x=no</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">成功运行结束后</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，您可能会看到建议使用包管理器安装额外系统包的消息。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">对于大量的</font></font><a href="https://github.com/sagemath/sage/issues/27330" data-hovercard-type="issue" data-hovercard-url="/sagemath/sage/issues/27330/hovercard"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 软件包</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，Sage 能够检测已安装的系统软件包是否适合与 Sage 一起使用；在这种情况下，Sage 不会从源构建另一个副本。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">有时，消息会建议安装系统上已安装的软件包。请参阅之前的配置消息或文件</font></font><code>config.log</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">以获取说明。此外，这些消息可能会建议安装实际上不可用的软件包；只有您的发行版的最新版本才会包含所有这些推荐的软件包。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：如果您选择安装附加系统软件包，重新运行</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">将测试安装的版本是否可用于 Sage；如果是，这将减少 Sage 所需的编译时间和磁盘空间。包的使用可以通过</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">参数进行调整（再次检查 的输出
</font></font><code>./configure --help</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">）。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">类型</font></font><code>make</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。就是这样！一切都是自动且非交互的。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您遵循上述说明，特别是关于安装（步骤 11）的输出推荐的系统软件包
</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，以及关于并行构建（步骤 10），则在现代计算机上构建 Sage 需要不到一小时。 （否则，可能需要更长的时间。）</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">该构建应该可以在所有完全支持的平台上正常运行。如果没有，我们想知道！</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">输入</font></font><code>./sage</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">来尝试一下。在 Sage 中，尝试例如</font></font><code>2 + 2</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">,
</font></font><code>plot(x^2)</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">来</font></font><code>plot3d(lambda x, y: x*y, (-1, 1), (-1, 1))</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
测试 2D 和 3D 中的简单计算和绘图。输入</font></font><kbd>Ctrl</kbd><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">+</font></font><kbd>D</kbd><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">或</font></font><code>quit</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">退出 Sage。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：键入</font></font><code>make ptestlong</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">测试文档中的所有示例（超过 200,000 行输入！）——这需要 10 分钟到几个小时。如果出现 2 到 3 次失败，请不要太担心，但请随时将</font></font><code>logs/ptestlong.log</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">包含错误的部分通过电子邮件发送到</font></font><a href="https://groups.google.com/group/sage-support" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sage-support 邮件列表</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。如果出现大量失败，则表明您的构建存在严重问题。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML 版本的文档</font></font><a href="https://doc.sagemath.org/html/en/index.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">是</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
在 Sage 编译过程中构建的，并驻留在目录中
</font></font><code>local/share/doc/sage/html/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。您可能想在浏览器中将其添加为书签。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：如果您想构建文档的 PDF 版本，请运行</font></font><code>make doc-pdf</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（这需要安装 LaTeX）。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"></font><code>./sage --optional</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：安装您感兴趣的可选软件包：通过键入或访问
</font></font><a href="https://doc.sagemath.org/html/en/reference/spkg/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">软件包文档页面</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">获取列表  </font><font style="vertical-align: inherit;">。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：例如，</font></font><code>sage</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">在您的目录中</font><font style="vertical-align: inherit;">创建指向已安装脚本的符号链接</font><font style="vertical-align: inherit;">。这将允许您通过从任何地方键入来启动 Sage </font><font style="vertical-align: inherit;">，而不必键入完整路径或导航到 Sage 目录并键入</font><font style="vertical-align: inherit;">。这可以通过运行来完成：</font></font><code>PATH</code><font style="vertical-align: inherit;"></font><code>/usr/local</code><font style="vertical-align: inherit;"></font><code>sage</code><font style="vertical-align: inherit;"></font><code>./sage</code><font style="vertical-align: inherit;"></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>$ sudo ln -s $(./sage -sh -c 'ls $SAGE_ROOT/venv/bin/sage') /usr/local/bin
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ sudo ln -s $(./sage -sh -c 'ls $SAGE_ROOT/venv/bin/sage') /usr/local/bin" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可选：将 SageMath 设置为现有 Jupyter 笔记本或 JupyterLab 安装中的 Jupyter 内核，如</font><font style="vertical-align: inherit;">
Sage 安装手册中的</font></font><a href="https://doc.sagemath.org/html/en/installation/launching.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">“启动 SageMath”部分所述。</font></font></a><font style="vertical-align: inherit;"></font></p>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">使用 PyPI 的替代安装</font></font></h2><a id="user-content-alternative-installation-using-pypi" class="anchor" aria-label="永久链接：使用 PyPI 的替代安装" href="#alternative-installation-using-pypi"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为了从 PyPI 在 Python 环境中安装 Sage，Sage 提供了
</font></font><code>pip</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可安装包</font></font><a href="https://pypi.org/project/sagemath-standard/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sagemath-standard</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">除非您需要将 Sage 安装到特定的现有环境中，否则我们建议创建并激活一个全新的虚拟环境，例如</font></font><code>~/sage-venv/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>        $ python3 -m venv ~/sage-venv
        $ source ~/sage-venv/bin/activate
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="        $ python3 -m venv ~/sage-venv
        $ source ~/sage-venv/bin/activate" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">作为第一个安装步骤，安装</font></font><a href="https://pypi.org/project/sage-conf/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sage_conf</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，它在以下子目录中构建各种必备包</font></font><code>~/.sage/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>        (sage-venv) $ python3 -m pip install -v sage_conf
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="        (sage-venv) $ python3 -m pip install -v sage_conf" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">安装成功后，驾驶室会提供各种Python包。您可以使用以下命令列出轮子：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>        (sage-venv) $ ls $(sage-config SAGE_SPKG_WHEELS)
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="        (sage-venv) $ ls $(sage-config SAGE_SPKG_WHEELS)" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果这给出错误，指出</font></font><code>sage-config</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">未找到，请检查该</font></font><code>pip install</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">命令可能已打印的任何消息。您可能需要调整您的</font></font><code>PATH</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，例如：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>        $ export PATH="$(python3 -c 'import sysconfig; print(sysconfig.get_path("scripts", "posix_user"))'):$PATH"
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="        $ export PATH=&quot;$(python3 -c 'import sysconfig; print(sysconfig.get_path(&quot;scripts&quot;, &quot;posix_user&quot;))'):$PATH&quot;" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">现在安装驾驶室中的软件包和</font></font><a href="https://pypi.org/project/sage-conf/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sage_setup</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
软件包，最后安装 Sage 库：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>        (sage-venv) $ python3 -m pip install $(sage-config SAGE_SPKG_WHEELS)/*.whl sage_setup
        (sage-venv) $ python3 -m pip install --no-build-isolation -v sagemath-standard
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="        (sage-venv) $ python3 -m pip install $(sage-config SAGE_SPKG_WHEELS)/*.whl sage_setup
        (sage-venv) $ python3 -m pip install --no-build-isolation -v sagemath-standard" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">上述说明安装了 Sage 的最新稳定版本。要安装最新的开发版本，请将开关添加</font></font><code>--pre</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">到
</font></font><code>python3 -m pip install</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
<p dir="auto"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">注意：</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> PyPI 还有各种其他</font></font><code>pip</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">可安装的软件包，其名称中带有“sage”一词。其中一些由 SageMath 项目维护，一些由 SageMath 用户出于各种目的提供，还有一些与 SageMath 完全无关。不要使用包
</font></font><code>sage</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和</font></font><code>sagemath</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。有关软件包的精选列表，请参阅
</font><font style="vertical-align: inherit;">Sage 参考手册的</font></font><a href="https://doc.sagemath.org/html/en/reference/spkg/index.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">软件包和功能一章。</font></font></a><font style="vertical-align: inherit;"></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">SageMath Docker 镜像</font></font></h2><a id="user-content-sagemath-docker-images" class="anchor" aria-label="永久链接：SageMath Docker 镜像" href="#sagemath-docker-images"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><a href="https://hub.docker.com/r/sagemath/sagemath" rel="nofollow"><img src="https://camo.githubusercontent.com/92009f5bffbf67de208fda407fa3f59a1091a906b1c12a413bedb44410cc6e59/687474703a2f2f646f636b6572692e636f2f696d6167652f736167656d6174682f736167656d617468" alt="Docker 状态" data-canonical-src="http://dockeri.co/image/sagemath/sagemath" style="max-width: 100%;"></a></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">SageMath 在 Docker Hub 上可用，可以通过以下方式下载：</font></font></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>docker pull sagemath/sagemath</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="docker pull sagemath/sagemath" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目前，仅稳定版本保持最新。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">故障排除</font></font></h2><a id="user-content-troubleshooting" class="anchor" aria-label="永久链接：故障排除" href="#troubleshooting"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您在构建 Sage 时遇到问题，请查看 Sage 安装指南，以及与</font><font style="vertical-align: inherit;">您要安装的版本相对应的</font></font><a href="https://wiki.sagemath.org/ReleaseTours" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 发布教程中特定于版本的 Sage 安装常见问题解答。</font></font></a><font style="vertical-align: inherit;"></font></p>
<p dir="auto"><font style="vertical-align: inherit;"></font><a href="https://ask.sagemath.org/questions/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请随时在SageMath 论坛
</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">或</font></font><a href="https://groups.google.com/forum/#!forum/sage-support" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sage 支持邮件列表</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中寻求帮助</font><font style="vertical-align: inherit;">。</font></font><a href="https://doc.sagemath.org/html/en/installation/troubles.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 安装指南中的故障排除部分
</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">提供
</font><font style="vertical-align: inherit;">
了有关提供哪些信息的说明，以便我们可以更有效地提供帮助。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为圣人做出贡献</font></font></h2><a id="user-content-contributing-to-sage" class="anchor" aria-label="永久链接：为 Sage 做出贡献" href="#contributing-to-sage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您想为 Sage 做出贡献，我们强烈建议您阅读
</font></font><a href="https://doc.sagemath.org/html/en/developer/index.html" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">开发人员指南</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 具有用以下语言编写的重要组件：C/C++、Python、Cython、Common Lisp、Fortran 和一些 Perl。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目录布局</font></font></h2><a id="user-content-directory-layout" class="anchor" aria-label="永久链接：目录布局" href="#directory-layout"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">简化的目录布局（仅重要文件/目录）：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>SAGE_ROOT                 Root directory (create by git clone)
├── build
│   └── pkgs              Every package is a subdirectory here
│       ├── 4ti2/
│       …
│       └── zlib/
├── configure             Top-level configure script
├── COPYING.txt           Copyright information
├── pkgs                  Source trees of Python distribution packages
│   ├── sage-conf
│   │   ├── sage_conf.py
│   │   └── setup.py
│   ├── sage-docbuild
│   │   ├── sage_docbuild/
│   │   └── setup.py
│   ├── sage-setup
│   │   ├── sage_setup/
│   │   └── setup.py
│   ├── sage-sws2rst
│   │   ├── sage_sws2rst/
│   │   └── setup.py
│   └── sagemath-standard
│       ├── bin/
│       ├── sage -&gt; ../../src/sage
│       └── setup.py
├── local  (SAGE_LOCAL)   Installation hierarchy for non-Python packages
│   ├── bin               Executables
│   ├── include           C/C++ headers
│   ├── lib               Shared libraries, architecture-dependent data
│   ├── share             Databases, architecture-independent data, docs
│   │   └── doc           Viewable docs of Sage and of some components
│   └── var
│       ├── lib/sage
│       │   ├── installed/
│       │   │             Records of installed non-Python packages
│       │   ├── scripts/  Scripts for uninstalling installed packages
│       │   └── venv-python3.9  (SAGE_VENV)
│       │       │         Installation hierarchy (virtual environment)
│       │       │         for Python packages
│       │       ├── bin/  Executables and installed scripts
│       │       ├── lib/python3.9/site-packages/
│       │       │         Python modules/packages are installed here
│       │       └── var/lib/sage/
│       │           └── wheels/
│       │                 Python wheels for all installed Python packages
│       │
│       └── tmp/sage/     Temporary files when building Sage
├── logs
│   ├── install.log       Full install log
│   └── pkgs              Build logs of individual packages
│       ├── alabaster-0.7.12.log
│       …
│       └── zlib-1.2.11.log
├── m4                    M4 macros for generating the configure script
│   └── *.m4
├── Makefile              Running "make" uses this file
├── prefix -&gt; SAGE_LOCAL  Convenience symlink to the installation tree
├── README.md             This file
├── sage                  Script to start Sage
├── src                   Monolithic Sage library source tree
│   ├── bin/              Scripts that Sage uses internally
│   ├── doc/              Sage documentation sources
│   └── sage/             The Sage library source code
├── upstream              Source tarballs of packages
│   ├── Babel-2.9.1.tar.gz
│   …
│   └── zlib-1.2.11.tar.gz
├── venv -&gt; SAGE_VENV     Convenience symlink to the virtual environment
└── VERSION.txt
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="SAGE_ROOT                 Root directory (create by git clone)
├── build
│   └── pkgs              Every package is a subdirectory here
│       ├── 4ti2/
│       …
│       └── zlib/
├── configure             Top-level configure script
├── COPYING.txt           Copyright information
├── pkgs                  Source trees of Python distribution packages
│   ├── sage-conf
│   │   ├── sage_conf.py
│   │   └── setup.py
│   ├── sage-docbuild
│   │   ├── sage_docbuild/
│   │   └── setup.py
│   ├── sage-setup
│   │   ├── sage_setup/
│   │   └── setup.py
│   ├── sage-sws2rst
│   │   ├── sage_sws2rst/
│   │   └── setup.py
│   └── sagemath-standard
│       ├── bin/
│       ├── sage -> ../../src/sage
│       └── setup.py
├── local  (SAGE_LOCAL)   Installation hierarchy for non-Python packages
│   ├── bin               Executables
│   ├── include           C/C++ headers
│   ├── lib               Shared libraries, architecture-dependent data
│   ├── share             Databases, architecture-independent data, docs
│   │   └── doc           Viewable docs of Sage and of some components
│   └── var
│       ├── lib/sage
│       │   ├── installed/
│       │   │             Records of installed non-Python packages
│       │   ├── scripts/  Scripts for uninstalling installed packages
│       │   └── venv-python3.9  (SAGE_VENV)
│       │       │         Installation hierarchy (virtual environment)
│       │       │         for Python packages
│       │       ├── bin/  Executables and installed scripts
│       │       ├── lib/python3.9/site-packages/
│       │       │         Python modules/packages are installed here
│       │       └── var/lib/sage/
│       │           └── wheels/
│       │                 Python wheels for all installed Python packages
│       │
│       └── tmp/sage/     Temporary files when building Sage
├── logs
│   ├── install.log       Full install log
│   └── pkgs              Build logs of individual packages
│       ├── alabaster-0.7.12.log
│       …
│       └── zlib-1.2.11.log
├── m4                    M4 macros for generating the configure script
│   └── *.m4
├── Makefile              Running &quot;make&quot; uses this file
├── prefix -> SAGE_LOCAL  Convenience symlink to the installation tree
├── README.md             This file
├── sage                  Script to start Sage
├── src                   Monolithic Sage library source tree
│   ├── bin/              Scripts that Sage uses internally
│   ├── doc/              Sage documentation sources
│   └── sage/             The Sage library source code
├── upstream              Source tarballs of packages
│   ├── Babel-2.9.1.tar.gz
│   …
│   └── zlib-1.2.11.tar.gz
├── venv -> SAGE_VENV     Convenience symlink to the virtual environment
└── VERSION.txt" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">有关更多详细信息，请参阅</font></font><a href="https://doc.sagemath.org/html/en/developer/coding_basics.html#files-and-directory-structure" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">我们的开发人员指南</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建系统</font></font></h2><a id="user-content-build-system" class="anchor" aria-label="永久链接：构建系统" href="#build-system"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">这是 Sage 软件发行版构建系统的简要总结。完整的 Sage 系统有两个组件——Sage Python 库及其相关的用户界面，以及 Sage 主要依赖项的较大软件分发版（对于用户系统未提供的那些依赖项）。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 的 Python 库是使用</font></font><code>setup.py</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">脚本构建和安装的，这是 Python 包的标准（Sage 的</font></font><code>setup.py</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">库很重要，但并不罕见）。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建系统的其余部分大部分涉及以正确的相互关系顺序构建 Sage 的所有依赖项。 Sage 包含的依赖项称为 SPKG（即“Sage 包”）并列在 下</font></font><code>build/pkgs</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"></font><code>Makefile</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 构建系统的主要入口点是源树根部的</font><font style="vertical-align: inherit;">顶层。</font><font style="vertical-align: inherit;">与大多数使用 autoconf 的普通项目不同（Sage 也这样做，如下所述），它</font></font><code>Makefile</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">不会生成。相反，它包含一些高级目标和与引导系统相关的目标。尽管如此，我们仍然</font></font><code>make &lt;target&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从源代码树的根开始运行——顶层中未明确定义的目标</font></font><code>Makefile</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">将传递到</font></font><code>build/make/Makefile</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">后者</font></font><code>build/make/Makefile</code> <em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">是</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">由 autoconf 生成的
</font></font><code>configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">脚本使用 中的模板生成的</font></font><code>build/make/Makefile.in</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。这包括构建 Sage 库本身的规则 ( </font></font><code>make sagelib</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">)，以及构建和安装每个 Sage 依赖项的规则 (例如</font></font><code>make gf2x</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">)。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果脚本</font></font><code>configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">本身尚未构建，则可以通过运行脚本来生成</font></font><code>bootstrap</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">（后者需要</font><font style="vertical-align: inherit;">安装</font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">GNU 自动工具</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">）。顶层</font></font><code>Makefile</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">也会自动处理这个问题。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">总而言之，</font></font><code>make python3</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">在源树的顶层运行命令如下所示：</font></font></p>
<ol dir="auto">
<li><code>make python3</code></li>
<li><font style="vertical-align: inherit;"></font><code>./bootstrap</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果</font></font><code>configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">需要更新则</font><font style="vertical-align: inherit;">运行</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
如果需要更新，</font></font><code>./configure</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请使用任何先前配置的选项</font><font style="vertical-align: inherit;">运行</font></font><code>build/make/Makefile</code><font style="vertical-align: inherit;"></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">将目录更改为</font></font><code>build/make</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">并运行</font></font><code>install</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">脚本 - 这只不过是运行的前端</font></font><code>make -f build/make/Makefile python3</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，它设置一些必要的环境变量并记录一些信息</font></font></li>
<li><code>build/make/Makefile</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">包含实际的构建规则</font></font><code>python3</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">；这包括</font></font><code>python3</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">首先构建所有的依赖项（以及它们的依赖项，递归地）；实际的软件包安装是通过</font></font><code>sage-spkg</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">程序执行的</font></font></li>
</ol>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">搬迁</font></font></h2><a id="user-content-relocation" class="anchor" aria-label="永久链接：搬迁" href="#relocation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">构建 Sage 后</font><font style="vertical-align: inherit;">不支持移动</font></font><code>SAGE_ROOT</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">或目录。</font></font><code>SAGE_LOCAL</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您确实移动了目录，则必须</font></font><code>make distclean</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从头开始重新运行并构建 Sage。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">对于系统范围的安装，您必须将 Sage 构建为“普通”用户，然后以 root 身份可以更改权限。请参阅</font></font><a href="https://doc.sagemath.org/html/en/installation/source.html#installation-in-a-multiuser-environment" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">安装指南</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
了解更多信息。</font></font></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">再分配</font></font></h2><a id="user-content-redistribution" class="anchor" aria-label="永久链接：重新分配" href="#redistribution"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">您的本地 Sage 安装几乎与任何“开发人员”安装完全相同。您可以对文档、源代码等进行更改，并像我们一样轻松地将完整结果打包以便重新分发。</font></font></p>
<ol dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">要使用当前安装的软件包制作二进制发行版，请访问</font></font><a href="https://github.com/sagemath/binary-pkg"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sagemath/binary-pkg</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">要制作您自己的 Sage 源 tarball，请输入：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>$ make dist
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ make dist" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">结果放置在目录中</font></font><code>dist/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
</ol>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">附带软件的更改</font></font></h2><a id="user-content-changes-to-included-software" class="anchor" aria-label="永久链接：对附带软件的更改" href="#changes-to-included-software"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sage 中包含的所有软件均受各自作者的版权保护，并根据与GPL 版本 3 或更高版本</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">兼容的开源许可证发布</font><font style="vertical-align: inherit;">。</font><font style="vertical-align: inherit;">有关更多详细信息，</font><font style="vertical-align: inherit;">请参阅</font></font><a href="/sagemath/sage/blob/develop/COPYING.txt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">COPYING.txt 。</font></font></a><font style="vertical-align: inherit;"></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">源代码位于目录中未修改（尽可能）的 tarball 中
</font></font><code>upstream/</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。其余的描述、版本信息、补丁和构建脚本位于随附的
</font></font><code>build/pkgs/&lt;packagename&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目录中。该目录是 Sage git 存储库的一部分。</font></font></p>
<p align="center" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
   版权所有 (C) 2005-2024 Sage 开发团队
</font></font></p>
<p align="center" dir="auto">
   <a href="https://www.sagemath.org" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">https://www.sagemath.org</font></font></a>
</p>
</article></div>
