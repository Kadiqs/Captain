import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
import { OrbitControls } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js";
import { FBXLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/FBXLoader.js";

const container3D = document.getElementById("container3D");
const modelStateText = document.getElementById('model-state-text');

let scene, camera, renderer, controls, loader;

function initScene() {
    scene = new THREE.Scene();
    scene.background = null;

    camera = new THREE.PerspectiveCamera(75, container3D.offsetWidth / container3D.offsetHeight, 0.1, 1000);
    camera.position.set(0, 1, 5);

    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(container3D.offsetWidth, container3D.offsetHeight);
    container3D.appendChild(renderer.domElement);

    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(500, 500, 500);
    scene.add(light);

    const ambientLight = new THREE.AmbientLight(0x333333);
    scene.add(ambientLight);

    controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 1, 0);
    controls.update();

    loader = new FBXLoader();

    loader.load(
        'my_model',
        (fbx) => {
            fbx.scale.set(0.015, 0.015, 0.015);
            fbx.position.y = -2;
            scene.add(fbx);
            modelStateText.textContent = 'Model State: Loaded';
        },
        (xhr) => {
            modelStateText.textContent = `Loading... ${Math.round((xhr.loaded / xhr.total) * 100)}%`;
        },
        (error) => {
            console.error('Error loading FBX:', error);
            modelStateText.textContent = 'Model State: Error';
        }
    );

    animate();
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
    if (camera && renderer && container3D) {
        camera.aspect = container3D.offsetWidth / container3D.offsetHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container3D.offsetWidth, container3D.offsetHeight);
    }
});

initScene();