from nuscenes.nuscenes import NuScenes

nusc = NuScenes(version='v1.0-mini', dataroot='/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/test_zone/dataset/nuscenes/data/sets/nuscenes', verbose=True)

my_scene_token = nusc.field2token('scene', 'name', 'scene-0061')[0]

# Renders the video for a particular channel.
nusc.render_scene_channel(my_scene_token, 'CAM_FRONT', out_path='/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/test_zone/dataset/nuscenes/sample_video.avi')

# Renders the video for all camera channels.
nusc.render_scene(my_scene_token, out_path='/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/test_zone/dataset/nuscenes/sample_video_6_cam.avi')

