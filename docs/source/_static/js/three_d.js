import * as THREE from "three";

import {OrbitControls} from "three/addons/controls/OrbitControls.js";
import {FBXLoader} from "three/addons/loaders/FBXLoader.js";

// Canvas
document.onreadystatechange = () => {
  if (document.readyState === "complete") {
    // Remove this element from Sphinx template layout to make the canvas full screen
    document.querySelector(".md-tabs").remove();

    // There is a rst include file in every hardware document, that adds a button, and when that page is loaded
    // the JS on that page will add the query parameter to the button/h3/section id, to identify what product it is.
    // the query parameter is used here, to let three.js to pick up the correct 3D model file in the _static folder.
    const urlSearchParams = new URLSearchParams(window.location.search);
    const params = Object.fromEntries(urlSearchParams.entries());
    const fbx_file = "/_static/3d_models/" + params.productModel + ".fbx";

    let camera, scene, renderer;

    init();
    animate();

    function init() {
      // Add 3D view to HTML document tree and remove some node from Sphinx layout
      const container = document.createElement('div');
      document.querySelector(".md-container").appendChild(container);
      document.querySelector(".md-main").remove();

      camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 2000);
      camera.position.set(100, 200, 300);

      scene = new THREE.Scene();
      scene.background = new THREE.Color(0xa0a0a0);
      scene.fog = new THREE.Fog(0xa0a0a0, 200, 1000);

      const hemiLight = new THREE.HemisphereLight(0xdddddd, 0x666666, 6.5);
      hemiLight.position.set(0, 200, 0);
      scene.add(hemiLight);

      const dirLight = new THREE.DirectionalLight(0xffffff, 1.5);
      dirLight.position.set(0, 200, 100);
      dirLight.castShadow = true;
      dirLight.shadow.camera.top = 180;
      dirLight.shadow.camera.bottom = -100;
      dirLight.shadow.camera.left = -120;
      dirLight.shadow.camera.right = 120;
      scene.add(dirLight);

      // ground
      const mesh = new THREE.Mesh(new THREE.PlaneGeometry(2000, 2000), new THREE.MeshPhongMaterial({
        color: 0x999999,
        depthWrite: false
      }));
      mesh.rotation.x = -Math.PI / 2;
      mesh.receiveShadow = true;
      scene.add(mesh);

      // Add grid to view
      const grid = new THREE.GridHelper(100, 3, 0x000000, 0x000000);
      grid.material.opacity = 0.8;
      grid.material.transparent = true;
      scene.add(grid);

      // Load 3D model
      const loader = new FBXLoader();
      loader.load(fbx_file, function (object) {
        object.traverse(function (child) {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
          }
        });
        scene.add(object);
      });

      renderer = new THREE.WebGLRenderer({antialias: true});
      renderer.setPixelRatio(window.devicePixelRatio);
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.shadowMap.enabled = true;
      container.appendChild(renderer.domElement);

      const controls = new OrbitControls(camera, renderer.domElement);
      controls.target.set(0, 0, 0);
      controls.update();

      window.addEventListener('resize', onWindowResize);
    }

    function onWindowResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }

    function animate() {
      requestAnimationFrame(animate);
      renderer.render(scene, camera);
    }
  }
};