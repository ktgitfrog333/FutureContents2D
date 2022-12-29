using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Title.Common;

namespace Title.Audio
{
    /// <summary>
    /// SEのプレイヤー
    /// </summary>
    public class SfxPlayer : MonoBehaviour, ITitleGameManager, ISfxPlayer
    {
        /// <summary>効果音のクリップ</summary>
        [SerializeField] private AudioClip[] clip;

        /// <summary>オーディオソース用のプレハブ</summary>
        [SerializeField] private GameObject sFXChannelPrefab;
        /// <summary>プール用</summary>
        private Transform _transform;
        /// <summary>プール済みのオーディオ情報マップ</summary>
        private Dictionary<ClipToPlay, int> _sfxIdxDictionary = new Dictionary<ClipToPlay, int>();

        public void OnStart()
        {
            if (_transform == null)
                _transform = transform;
        }

        public void PlaySFX(ClipToPlay clipToPlay)
        {
            try
            {
                if ((int)clipToPlay <= (clip.Length - 1))
                {
                    var audio = GetSFXSource(clipToPlay);
                    audio.clip = clip[(int)clipToPlay];

                    // SEを再生
                    audio.Play();
                }
            }
            catch (System.Exception e)
            {
                Debug.Log("対象のファイルが見つかりません:[" + clipToPlay + "]");
                Debug.Log(e);
            }
        }

        /// <summary>
        /// SFXのキーから対象のオーディオソースを取得する
        /// </summary>
        /// <param name="key">ClipToPlayのキー</param>
        /// <returns>オーディオソース</returns>
        private AudioSource GetSFXSource(ClipToPlay key)
        {
            if (!_sfxIdxDictionary.ContainsKey(key))
            {
                var sfx = Instantiate(sFXChannelPrefab);
                sfx.transform.parent = _transform;
                _sfxIdxDictionary.Add(key, _transform.childCount - 1);
                return sfx.GetComponent<AudioSource>();
            }
            return _transform.GetChild(_sfxIdxDictionary[key]).GetComponent<AudioSource>();
        }
    }

}
