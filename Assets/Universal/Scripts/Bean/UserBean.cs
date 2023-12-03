using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Universal.Common;

namespace Universal.Bean
{
    [System.Serializable]
    /// <summary>
    /// ユーザー情報を保持するクラス
    /// T.B.D 管理データから配列数を管理
    /// </summary>
    public class UserBean
    {
        /// <summary>
        /// デフォルトのシーンID
        /// </summary>
        private static readonly int SCENEID_DEFAULT = 1;
        
        /// <summary>
        /// 全てのシーンID
        /// </summary>
        private readonly int SCENEID_ALL = 1;
        
        /// <summary>
        /// クリアステータスの長さ
        /// </summary>
        private readonly static int STATELENGTH = 15;
        
        /// <summary>
        /// デフォルトのクリアステータス
        /// </summary>
        private readonly int[] STATE_DEFAULT = {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        
        /// <summary>
        /// 全解放時のクリアステータス
        /// </summary>
        private readonly int[] STATE_ALL = {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2};

        /// <summary>
        /// シーンID
        /// </summary>
        public int sceneId = SCENEID_DEFAULT;
        
        /// <summary>
        /// クリアステータス
        /// </summary>
        public int[] state = new int[STATELENGTH];
        
        /// <summary>
        /// オーディオボリュームインデックス
        /// </summary>
        public int audioVolumeIndex = 5;
        
        /// <summary>
        /// BGMボリュームインデックス
        /// </summary>
        public int bgmVolumeIndex = 5;
        
        /// <summary>
        /// SEボリュームインデックス
        /// </summary>
        public int seVolumeIndex = 5;
        
        /// <summary>
        /// 振動有効インデックス
        /// </summary>
        public int vibrationEnableIndex = 0;

        /// <summary>
        /// ユーザー情報を保持するクラス
        /// </summary>
        public UserBean(EnumLoadMode enumLoadMode=EnumLoadMode.Continue)
        {
            switch (enumLoadMode)
            {
                case EnumLoadMode.Continue:
                    break;
                case EnumLoadMode.Default:
                    sceneId = SCENEID_DEFAULT;
                    state = STATE_DEFAULT;

                    break;
                case EnumLoadMode.All:
                    sceneId = SCENEID_ALL;
                    state = STATE_ALL;

                    break;
            }
        }

        /// <summary>
        /// ユーザー情報を保持するクラス
        /// </summary>
        public UserBean(UserBean userBean)
        {
            sceneId = userBean.sceneId;
            state = userBean.state;
            audioVolumeIndex = userBean.audioVolumeIndex;
            bgmVolumeIndex = userBean.bgmVolumeIndex;
            seVolumeIndex = userBean.seVolumeIndex;
            vibrationEnableIndex = userBean.vibrationEnableIndex;
        }
    }
}
