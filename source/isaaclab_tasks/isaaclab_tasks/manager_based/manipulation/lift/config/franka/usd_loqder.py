from pxr import Usd, UsdGeom, UsdPhysics

usd_path = "/home/pbd/IsaacLab/scripts/reinforcement_learning/rl_games/my_data/No19_koala_no_march/mesh_refined.usd"
stage = Usd.Stage.Open(usd_path)

for prim in stage.Traverse():
    print(f"Prim: {prim.GetName()} ({prim.GetTypeName()})")

    # Bounding box
    geom = UsdGeom.Mesh(prim)
    if geom:
        bbox = geom.ComputeExtent()
        print(f"  Bounding Box: {bbox}")

    # Check for RigidBodyAPI
    if UsdPhysics.RigidBodyAPI.HasAPI(prim):
        rb = UsdPhysics.RigidBodyAPI(prim)
        # Mass
        mass_attr = rb.GetPrim().GetAttribute('physics:mass')
        friction_attr = rb.GetPrim().GetAttribute('physics:friction')
        restitution_attr = rb.GetPrim().GetAttribute('physics:restitution')
        print(f"  Mass: {mass_attr.Get() if mass_attr else 'N/A'}")
        print(f"  Friction: {friction_attr.Get() if friction_attr else 'N/A'}")
        print(f"  Restitution: {restitution_attr.Get() if restitution_attr else 'N/A'}")
