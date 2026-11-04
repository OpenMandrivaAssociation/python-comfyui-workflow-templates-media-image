Name:		python-comfyui-workflow-templates-media-image
Version:	0.3.160
Release:	1
Summary:	Image workflow preview media for ComfyUI
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates-media-image/comfyui_workflow_templates_media_image-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Preview images for ComfyUI's image workflow templates.
These are upstream media assets, not model weights.

%files
%{py_sitedir}/comfyui_workflow_templates_media_image
%{py_sitedir}/comfyui_workflow_templates_media_image-*.*-info
